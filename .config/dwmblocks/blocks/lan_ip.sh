#!/bin/bash

# printf "%s" "$(ip a s enp42s0 | egrep -o 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'  | awk '{print $2}')"
printf "%s" "$(ip route | grep src | head -n 1 | awk '{split($3, a, /\./); print $9 "->" a[4]}')"
