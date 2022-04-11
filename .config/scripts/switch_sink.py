import subprocess
import re
# xprop _NET_WM_PID | sed 's/_NET_WM_PID(CARDINAL) = //' | echo `cat`
sinks  = [
    "Monitor",
    "alsa_output.usb-Kingston_HyperX_Cloud_Alpha_S_000000000001-00.analog-stereo"
]

def decode_output(input: bytes) -> str:
    return input.decode('utf-8').strip()

def get_win_pid() -> int:
    xprop_out = subprocess.run(
    ["xprop", "_NET_WM_PID"], 
    capture_output=True
    )
    if xprop_out.stdout:
        return int(decode_output(xprop_out.stdout).split(' ')[-1])

def get_sink_inputs():
    pactl_out = subprocess.run(
        ["pactl", "list",  "sink-inputs"],
        capture_output=True
    )
    if pactl_out.stdout:
        pactl_out = decode_output(pactl_out.stdout)
        sink_input_ids = re.findall('Sink Input #(\w+)', pactl_out)
        sink_input_pid = re.findall('application\.process\.id \= "(\d*)"', pactl_out)
        sink_input_sink = re.findall('Sink: (\d*)', pactl_out)
        sink_input_info = dict()
        for pid,_id,sink in zip(sink_input_pid, sink_input_ids, sink_input_sink):
            sink_input_info[int(pid)] = [_id, sink] # process_id:[input_id, sink_id]
        return(sink_input_info)

def get_sinks():
    pactl_out = subprocess.run(
        ["pactl", "list","short",  "sinks"],
        capture_output=True
    )
    if pactl_out.stdout:
        pactl_out = list(map(lambda x: x.split('\t'), decode_output(pactl_out.stdout).split('\n')))
        sinks = [tuple(i[0:2]) for  i in pactl_out]
        sink_info = dict(sinks)
        return(sink_info)

"""
1. choose a window
2. set the sink for that window to other on in sinks var
"""

win_pid = get_win_pid()

# get all current sink-inputs and sinks
all_sinks = get_sinks()

move_to = None
sink_inputs = get_sink_inputs()
if win_pid in sink_inputs.keys():
    sink_input = sink_inputs[win_pid]
    # check current sink
    if all_sinks[str(sink_input[1])] == sinks[0]:
        for key,value in all_sinks.items():
            if value == sinks[1]:
                move_to = key
    else:
        for key,value in all_sinks.items():
            if value == sinks[0]:
                move_to = key  
    subprocess.run(
        ["pactl","move-sink-input", str(sink_input[0]), str(move_to)]
    )
