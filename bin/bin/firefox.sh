#!/bin/bash

kill `pidof -x $0 -o %PPID`

launch_firefox() {
    FIRE=`pidof firefox | wc -w`
    if [ "$FIRE" -lt "1" ]
    then echo "launching firefox" ; firefox
    else echo "firefox is running" 
    fi
}

while true
do launch_firefox ; sleep 5
done
