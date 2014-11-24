#!/bin/bash

killall compton

compton --config "$HOME/.i3/compton.transperancy.conf" &

i3-msg '[ class=".*" ] border normal'

# Quick and dirty hack until I figure out how to change new_window.
bash -c "while true ; do sleep 3 && i3-msg '[ class=\".*\" ] border normal' ; done" &
