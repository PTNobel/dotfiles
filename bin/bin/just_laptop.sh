#!/bin/sh
#
# Sets only one monitor: the actual laptop.

xrandr --output LVDS1 --mode 1366x768 --pos 0x809 --rotate normal --primary

xrandr --output HDMI1 --off
xrandr --output VIRTUAL1 --off
xrandr --output DP1 --off
xrandr --output VGA1 --off
xrandr --setprovideroffloadsink radeon Intel

sh ~/.fehbg
sleep 3
sh ~/.fehbg
