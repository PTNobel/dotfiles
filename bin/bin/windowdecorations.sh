#!/bin/bash

if cat /proc/$(pgrep compton)/cmdline | grep transperancy ; then
  i3-msg '[ class=".*" ] border normal'
else
  echo nothing to do
fi
