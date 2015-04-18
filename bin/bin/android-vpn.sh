#!/bin/bash
#
# tethers an android phone to this computer using azilink

adb forward tcp:41927 tcp:41927

cd /usr/local/share/vpn.sh/

if wifi | grep on; then sudo wifi off; else
  sudo setsid openvpn azilink.ovpn
fi
sudo wifi on
