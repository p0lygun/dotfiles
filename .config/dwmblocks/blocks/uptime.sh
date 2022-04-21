#!/bin/bash
awk '{printf("UP %dh %dm",($1/60/60%24),($1/60%60))}' /proc/uptime