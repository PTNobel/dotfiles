#!/bin/bash
synclient  | grep TouchpadOff | grep 0 >/dev/null
STATE=$?
#ID=`xinput list | grep -Eo 'TouchPad\s*id\=[0-9]{1,2}' | grep -Eo '[0-9]{1,2}'`
#declare -i STATE
#STATE=`xinput list-props $ID|grep 'Device Enabled'|awk '{print $4}'`
if [ $STATE -eq 1 ]
then
   synclient TouchpadOff=0
   echo Touchpad Enabled
else
   synclient TouchpadOff=1
   echo Touchpad Disabled
fi