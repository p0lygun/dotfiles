import os
import subprocess
import re
import pathlib
def safe_cast(obj: object, new_type, default):
    try:
        return  new_type(obj)
    except ValueError:
        return default
    except TypeError:
        return default

counter_file = pathlib.Path("/tmp/dwm_spotify")
counter_file.touch(exist_ok=True)
with open(counter_file) as FILE:
    data = FILE.read().strip().split('\n')
    if len(data) == 2:
        value,track = data
    else:
        value='0'
        track=""

max_len =  safe_cast(os.getenv("DWM_SPOTIFY_MAX"), int, 15)
if len(value) == 0:
    value = 0
value = int(value)

command = """dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata"""
a = subprocess.run(command.split(' '), capture_output=True, check=True).stdout.decode('utf-8')



all_entries = re.findall('string "(.*?)"', a, flags=re.DOTALL)
matches = ["xesam:title", "xesam:artist"]
entries = []
try:
    for i in matches:
        entries.append(all_entries[all_entries.index(i)+1])
except ValueError:
    pass
except IndexError:
    pass
if entries[0] != track.strip():
    value = 0
final_string = ":".join(entries)+"  "

print(final_string[value:value+max_len].center(max_len))
#ffset = abs(len(final_string)-max_len)
value += 1
if value+max_len == len(final_string):
    value=0
with open(counter_file, 'w') as FILE:
    value = FILE.write(f"{value}\n{entries[0]}")
