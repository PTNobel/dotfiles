#!/bin/bash
#
# switches between my two keyboard layouts.

VARIANT=$(setxkbmap -query | awk '/variant/{print $2}')

if [ "$VARIANT" == "intl" ] ; then
  setxkbmap -layout us -variant ''
  setxkbmap -option caps:escape

else
  setxkbmap -layout us -variant intl #; echo " VARIANT = intl "
  setxkbmap -option caps:escape
fi
