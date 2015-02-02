#!/bin/bash

if pidof redshift; then
    echo redshift is running
    cd /proc
    for i in $(pidof redshift) ; do
    echo $i
    cd $i
    if [ $(strings ./environ | grep DISPLAY) = "DISPLAY=${DISPLAY}" ]; then
        OPTIONS=$(cat cmdline)
        kill $i
    fi
    done
    if echo $OPTIONS | grep redshift.alt.conf >/dev/null ; then
        redshift &
    else
        redshift -c $HOME/.config/redshift.alt.conf & 
    fi
else 
    echo redshift lauching
    redshift &
fi
