#!/bin/bash

dunst -config ~/.i3/dunstrc 2>&1 &

sleep 10

kill $!


setsid dunst -config ~/.i3/dunstrc 2>&1 &
