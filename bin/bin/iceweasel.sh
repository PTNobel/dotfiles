#!/bin/bash
#
# keeps iceweasel running.

for i in $(pidof -x firefox.sh -o %PPID) ; do
    if strings /proc/"$i"/environ | grep DISPLAY | grep "${DISPLAY}" >/dev/null ; then
        kill "$i"
    fi
done

launch_iceweasel() {
    ICE=$(pidof iceweasel | wc -w)
    if [ "$ICE" -lt "1" ]
    then echo "launching iceweasel" ; iceweasel
    else echo "iceweasel is running"
    fi
}

while true
do launch_iceweasel ; sleep 3
done
