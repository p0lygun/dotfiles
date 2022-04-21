import os
import subprocess
vol=subprocess.run(["pamixer", "--get-volume"], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
if os.getenv("BUTTON") == "2":
    os.system(f'dunstify "Volume: " -h int:value:{vol}')
print(vol)
