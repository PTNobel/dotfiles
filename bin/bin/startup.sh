#!/bin/bash

if [[ -f /tmp/startup."$DISPLAY".sh.log ]] ; then exit; fi

echo ran > /tmp/startup."$DISPLAY".sh.log

libreoffice --writer ~/Templates/APEC\ Essay\ Test.ott
