#!/bin/bash


dunstify "Volume: " -h int:value:"$(pamixer --get-volume)"


