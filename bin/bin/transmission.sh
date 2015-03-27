#!/bin/bash

kill "$(pidof -x "$0" -o %PPID)"

killall transmission-gtk

while true
do transmission-gtk -m
done
