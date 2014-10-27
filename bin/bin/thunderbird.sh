#!/bin/bash

launch_thunderbird() {
    pidof thunderbird
    if [ $? -eq 1 ]
    then echo "launching thunderbird" ; thunderbird
    else echo "thunderbird is running" 
    fi
}

while true
do launch_thunderbird ; sleep 5
done
