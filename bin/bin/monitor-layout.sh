#!/bin/sh
if xrandr --output HDMI1 --mode 1920x1080 --pos 1366x0 --rotate normal --primary; then
    xrandr --output LVDS1 --mode 1366x768 --pos 0x809 --rotate normal
else
    xrandr --output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal --primary ; xrandr --output HDMI1 --off
fi
xrandr --output VIRTUAL1 --off
xrandr --output DP1 --off
xrandr --output VGA1 --off
xrandr --setprovideroffloadsink radeon Intel
