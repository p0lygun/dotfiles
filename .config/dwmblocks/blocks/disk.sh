#!/bin/bash
printf "home %s" "$(df -h /dev/nvme0n1p3 | awk '{print $5}' | tail -n 1)"