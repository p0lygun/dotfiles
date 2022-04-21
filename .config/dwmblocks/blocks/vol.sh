#!/bin/bash

printf "VOL: %s" "$(pamixer --get-volume-human)"
