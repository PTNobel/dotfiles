#!/bin/bash

adb forward tcp:41927 tcp:41927

cd /usr/local/share/vpn.sh/

if wifi | grep on; then sudo wifi off; else

sudo openvpn azilink.ovpn
fi
sudo wifi on
