#!/bin/bash
#
# keeps transmission-gtk running.

kill "$(pidof -x "$0" -o %PPID)"

killall transmission-gtk

while true
do transmission-gtk -m
done
