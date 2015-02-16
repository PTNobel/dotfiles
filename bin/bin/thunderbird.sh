#!/bin/bash

for i in $(pidof -x firefox.sh -o %PPID) ; do
    if strings /proc/$i/environ | grep DISPLAY | grep "DISPLAY=${DISPLAY}" >/dev/null ; then
        kill $i
    fi
done

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
