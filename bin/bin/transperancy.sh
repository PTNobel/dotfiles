#!/bin/bash
#
# switches the window transperancy and window decorations.

if grep transperancy /proc/"$(pgrep compton)"/cmdline; then
  killall compton
  compton --config "$HOME/.i3/compton.conf" &
  i3-msg '[ class=".*" ] border pixel'
else
killall compton

compton --config "$HOME/.i3/compton.transperancy.conf" &

i3-msg '[ class=".*" ] border normal'

# Quick and dirty hack until I figure out how to change new_window.
fi
for i in $(pgrep bash); do
    cd /proc/"$i"
    grep windowdecorations.sh cmdline && kill "$i"
done
bash -c "while true ; do sleep 1 && windowdecorations.sh &>/dev/null ; done" &
