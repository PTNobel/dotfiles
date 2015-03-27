#!/bin/bash

for i in $(pidof -x firefox.sh -o %PPID) ; do
    if strings /proc/"$i"/environ | grep DISPLAY | grep "${DISPLAY}" >/dev/null ; then
        kill "$i"
    fi
done

while true ; do
    if [ "$(pidof urxvtd | wc -w)" -lt 1 ]; then
        urxvtd
else
    sleep 10
fi
done
