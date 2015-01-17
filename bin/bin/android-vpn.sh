#!/bin/bash

adb forward tcp:41927 tcp:41927

cd /usr/local/share/vpn.sh/

sudo openvpn azilink.ovpn
