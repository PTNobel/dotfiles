#!/bin/bash
#
# starts mpd.

killall mpd &>/dev/null

#sleep 1

mpd ~/.config/mpd/mpd.conf || mpd ~/.config/mpd/mpd.conf.offline
if [ $? -eq 0 ]; then
  mpd #~/.config/mpd/mpd.conf.online
else
  mpd ~/.config/mpd/mpd.conf.offline
fi
