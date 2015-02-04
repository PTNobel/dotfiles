#!/bin/bash

if pidof xautolock >/dev/null ; then
    for i in $(pidof xautolock) ; do
        echo $i
        cd $i
        if [ $(strings ./environ | grep DISPLAY) = "DISPLAY=${DISPLAY}" ]; then
            SWITCH_STATES=1
            if [ $SWITCH_STATES == 1 ] ; then
                kill $i
                xset -dpms
            else
                echo dazed and confused
                echo running away into the woods.
                echo good bye.
                exit 5
            fi
        else
            SWITCH_STATES=0
        fi
    done
else
    SWITCH_STATES=0
fi

if [ $SWITCH_STATES == 0 ]; then
    xautolock -time 5 -locker 'i3exit inactive_lock' &
    xset +dpms
fi
