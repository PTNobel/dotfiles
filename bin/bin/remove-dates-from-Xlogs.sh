#!/bin/zsh
# 
# So to use this script, take a copy of Xorg.#.log (where # is a number)
# and open it in vim, possibly vi too (I haven't tested it in vi)
# and then launch this script in a different terminal, move the mouse 
# over the terminal with vim and watch it work. Consider getting some tea.
#
#


sleep 3
while sleep .3; cat "$1" | grep "^\[" >|/dev/null ; do
    xdotool key slash asciicircum backslash bracketleft Return # /^\[
    xdotool key 5 d w
    xdotool key colon w Return
done
notify-send Done\ with\ this\ file
