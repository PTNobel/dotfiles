#!/bin/bash

killall -q conky

if xrandr | grep '*' | grep '^   1366x768' &>/dev/null
then setsid conky -c "$HOME"/.conkyrc-2 &>/dev/null &
fi

if xrandr | grep '*' | grep '^   1920x1080' &>/dev/null
then setsid conky &>/dev/null &
fi
