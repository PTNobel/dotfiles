#!/bin/bash
#
# Launches CivV.


function CivV {
  steam steam://rungameid/8930 &
  #cd /home/parth/.local/share/Steam/SteamApps/common/Sid\ Meier\'s\ Civilization\ V
  #/home/parth/.local/share/Steam/SteamApps/common/Sid\ Meier\'s\ Civilization\ V/Civ5XP
  echo "steam started"
  until [ "$(pidof steam | wc -w)" -ge 3 ] ; do
    sleep 5
  done
  until [ "$(pidof steam | wc -w)" -le 2 ] ; do
    sleep 30
  done
}

CivV &
