#!/bin/bash
#
# keeps icecat running.

for i in $(pidof -x icecat.sh -o %PPID) ; do
  if strings /proc/"$i"/environ | grep DISPLAY | grep "${DISPLAY}" >/dev/null ; then
    kill "$i"
  fi
done

function launch_icecat {
  ICE=$(pidof icecat | wc -w)
  if [ "$ICE" -lt "1" ]
  then echo "launching icecat" ; icecat
  else echo "icecat is running"
  fi
}

while true
do launch_icecat ; sleep 3
done
