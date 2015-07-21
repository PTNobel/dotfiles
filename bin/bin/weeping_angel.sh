#!/bin/bash
#
# swithces through Weeping Angel photos.

function angels {
  feh --bg-scale ~/Pictures/Weeping\ Angel/1.JPG
  sleep 5
  feh --bg-scale ~/Pictures/Weeping\ Angel/2.JPG
  sleep 5
  feh --bg-scale ~/Pictures/Weeping\ Angel/3.JPG
  sleep 5
  feh --bg-scale ~/Pictures/Weeping\ Angel/4.JPG
  sleep 5
  feh --bg-scale ~/Pictures/Weeping\ Angel/5.JPG
  sleep 5
}

while true ; do angels ; done
