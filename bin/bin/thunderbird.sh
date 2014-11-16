#!/bin/bash

kill `pidof -x $0 -o %PPID`

launch_thunderbird() {
    THUNDER=`pidof thunderbird | wc -w`
    if [ "$THUNDER" -lt "1" ]
    then echo "launching thunderbird" ; thunderbird
    else echo "thunderbird is running" 
    fi
}

while true
do launch_thunderbird ; sleep 5
done
