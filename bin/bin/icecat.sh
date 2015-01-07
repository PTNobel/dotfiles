#!/bin/bash

kill `pidof -x $0 -o %PPID`

launch_icecat() {
    FIRE=`pidof icecat | wc -w`
    if [ "$FIRE" -lt "1" ]
    then echo "launching icecat" ; icecat
    else echo "icecat is running" 
    fi
}

while true
do launch_icecat ; sleep 5
done
