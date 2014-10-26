#!/bin/bash

killall mpd &>/dev/null

#sleep 1

mpd ~/.config/mpd/mpd.conf || mpd ~/.confg/mpd/mpd.conf.offline
if [ $? -eq 0 ]; then
mpd #~/.config/mpd/mpd.conf.online
else mpd ~/.config/mpd/mpd.conf
fi
