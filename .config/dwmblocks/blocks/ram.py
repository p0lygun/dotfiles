import re
meminfo = open('/proc/meminfo').read()
total = int(re.findall("MemTotal:\s*(\d+)",meminfo)[0])
free = int(re.findall("MemFree:\s*(\d+)",meminfo)[0])
buffers = int(re.findall("MemAvailable:\s*(\d+)",meminfo)[0])
buffers = int(re.findall("Buffers:\s*(\d+)",meminfo)[0])
cached = int(re.findall("Cached:\s*(\d+)",meminfo)[0])
d = (total - free - buffers - cached) / 1000000
prefix = "RAM: "
ram=''
if d > 1:
    ram += f"{round(d, 1)} GB"
else:
    ram += f"{int(round(d*1000, 1))} MB"
print(prefix+ram)
