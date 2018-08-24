#!/bin/bash
#
# Turns the monitors on as needed.

if ! xrandr | grep "^HDMI" | grep disconnected; then
  xrandr --output HDMI1 --mode 1920x1080 --pos 1920x0 --rotate normal --primary
  xrandr --output eDP1 --mode 1920x1080 --pos 0x900 --rotate normal
else
  xrandr --output eDP1 --mode 1920x1080 --pos 0x0 --rotate normal
  xrandr --output HDMI1 --off
fi
xrandr --output VIRTUAL1 --off
sh ~/.fehbg
sleep 3
sh ~/.fehbg
