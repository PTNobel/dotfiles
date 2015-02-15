#!/bin/bash

setsid dunst -config ~/.i3/dunstrc 2>&1 | grep "Unknown keyboard shortcut: mod4+dead_grave"
