#!/bin/bash
cat /proc/stat |grep cpu |tail -1|awk '{print ($5*100)/($2+$3+$4+$5+$6+$7+$8+$9+$10)}'|printf "CPU: %.2f%%" "$(awk '{print 100-$1}')"