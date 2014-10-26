#!/bin/bash

while true
do if [ `pidof urxvtd | wc -w` -lt 1 ]
then urxvtd
else sleep 10
fi
done
