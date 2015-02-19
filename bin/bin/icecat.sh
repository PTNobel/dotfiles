#!/bin/bash

for i in $(pidof -x firefox.sh -o %PPID) ; do
    if strings /proc/$i/environ | grep DISPLAY | grep "DISPLAY=${DISPLAY}" >/dev/null ; then
        kill $i
    fi
done

launch_icecat() {
    ICE=`pidof icecat | wc -w`
    if [ "$ICE" -lt "1" ]
    then echo "launching icecat" ; icecat
    else echo "icecat is running"
    fi
}

while true
do launch_icecat ; sleep 3
done
