#!/bin/bash
#
# Launches CivV.

CivV() {
  steam steam://rungameid/8930 &
  echo "steam started"
  until [ "$(pidof steam | wc -w)" -ge 3 ] ; do
    sleep 5
  done
  until [ "$(pidof steam | wc -w)" -le 2 ] ; do
    sleep 30
  done
}

CivV &
