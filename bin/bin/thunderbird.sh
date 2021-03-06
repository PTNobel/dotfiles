#!/bin/bash
#
# Keeps thunderbird running.

for i in $(pidof -x thunderbird.sh -o %PPID) ; do
  if strings /proc/"$i"/environ | grep DISPLAY | grep "DISPLAY=${DISPLAY}" >/dev/null ; then
    kill "$i"
  fi
done

function launch_thunderbird {
  THUNDER=$(pidof thunderbird | wc -w)
  if [ "$THUNDER" -lt "1" ]; then
    echo "launching thunderbird" ; thunderbird
  else
    echo "thunderbird is running"
  fi
}

while true; do
  launch_thunderbird
  sleep 5
done
