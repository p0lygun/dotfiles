#!/bin/bash
choice="$(echo -e 'Reboot\nLogout\nShutdown' | rofi -location 3 -dmenu -sidebar-mode -i -p '➡' -mesg "$(uptime -p)")"
case $choice in
    Reboot) sudo reboot ;;
    Logout) sudo logout ;;
    Shutdown) sudo shutdown now ;;
esac