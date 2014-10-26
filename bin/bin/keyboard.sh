#!/bin/bash

VARIANT=`setxkbmap -query | awk '/layout/{print $2}'`

if [ "$VARIANT" == "intl" ]

then setxkbmap -layout us -variant

else setxkbmap -layout us -variant intl #; echo " VARIANT = intl "


fi
