#!/bin/bash

setsid dunst -config ~/.i3/dunstrc 2>&1

sleep 10

killall dunst


setsid dunst -config ~/.i3/dunstrc 2>&1
