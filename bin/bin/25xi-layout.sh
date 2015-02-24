#!/bin/sh
xrandr --output HDMI1 --mode 1920x1080 --pos 1366x0 --rotate normal --primary
if [ $? -eq 1 ]; then
    xrandr --output LVDS1 --mode 1366x768 --pos 0x809 --rotate normal --primary
    xrandr --output HDMI1 --off
else
    xrandr --output HDMI1 --mode 1920x1080 --pos 1366x0 --rotate normal --primary
    xrandr --output LVDS1 --off
fi
xrandr --output VIRTUAL1 --off
xrandr --output DP1 --off
xrandr --output VGA1 --off
xrandr --setprovideroffloadsink radeon Intel
