#!/bin/bash
#
# changes the window decorations.

if grep transperancy /proc/"$(pgrep compton)"/cmdline ; then
  i3-msg '[ class=".*" ] border normal'
else
  echo "nothing to do"
fi
