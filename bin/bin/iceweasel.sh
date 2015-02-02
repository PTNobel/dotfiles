#!/bin/bash

kill `pidof -x $0 -o %PPID`

launch_iceweasel() {
    ICE=`pidof iceweasel | wc -w`
    if [ "$ICE" -lt "1" ]
    then echo "launching iceweasel" ; iceweasel
    else echo "iceweasel is running" 
    fi
}

while true
do launch_iceweasel ; sleep 3
done
