#!/bin/bash
#
# Switches between redshift confs.

if pidof redshift; then
    echo redshift is running
    cd /proc || exit 54
    for i in $(pidof redshift) ; do
    echo "$i"
    cd "$i" || exit 54
    if [ "$(strings ./environ | grep DISPLAY)" = "DISPLAY=${DISPLAY}" ]; then
        OPTIONS=$(cat cmdline)
        kill "$i"
    fi
    done
    if echo "$OPTIONS" | grep redshift.alt.conf >/dev/null ; then
        redshift -c "$HOME"/.config/redshift.off.conf &
    elif echo "$OPTIONS" | grep redshift.off.conf ; then
      redshift &
    else
        redshift -c "$HOME"/.config/redshift.alt.conf &
    fi
else
    echo redshift lauching
    redshift &
fi
