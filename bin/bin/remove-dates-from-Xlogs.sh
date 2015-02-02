#!/bin/zsh

sleep 3 ; while sleep .3; cat Xorg.0.log.old.2 | grep "^\[" >|/dev/null ; do xdotool key n ;  xdotool key 5 d w ; xdotool key colon w Return ; done ; notify-send Done\ with\ this\ file
