#!/bin/bash

setsid dunst -config ~/.i3/dunstrc 2>&1 | grep "Unknown keyboard shortcut: mod4+dead_grave"
if [ $? -eq 0 ] ; then
    echo if statement
    killall dunst
    setsid dunst -config ~/.i3/grave.dunstrc | grep Unknown 
fi
