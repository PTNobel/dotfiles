#!/bin/bash
#
# keeps firefox running.

for i in $(pidof -x firefox.sh -o %PPID) ; do
  if strings /proc/"$i"/environ | grep DISPLAY | grep "${DISPLAY}" >/dev/null ; then
    kill "$i"
  fi
done

function launch_firefox {
  FIRE=$(pidof firefox | wc -w)
  if [ "$FIRE" -lt "1" ]; then
    echo "launching firefox"
    firefox
  else
    echo "firefox is running"
  fi
}

while true; do
  launch_firefox
  sleep 5
done
