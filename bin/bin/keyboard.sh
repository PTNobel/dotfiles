#!/bin/bash

VARIANT=`setxkbmap -query | awk '/variant/{print $2}'`

if [ "$VARIANT" == "intl" ]

then setxkbmap -layout us -variant ''

else setxkbmap -layout us -variant intl #; echo " VARIANT = intl "


fi
