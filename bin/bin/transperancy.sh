#!/bin/bash

killall compton

compton --config "$HOME/.i3/compton.transperancy.conf" &

i3-msg '[ class=".*" ] border normal'
