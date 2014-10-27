#!/bin/bash

launch_firefox() {
    pidof firefox
    if [ $? -ge 1 ]
    then echo "launching firefox" ; firefox
    else echo "firefox is running" 
    fi
}

while true
do launch_firefox ; sleep 5
done
