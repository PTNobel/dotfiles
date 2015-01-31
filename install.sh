#!/bin/bash

stow_wrapper(){
    for i in $(cat "$MANIFEST_FILE"); do
        if [ -d $i ] || true ; then
            #echo $i $1
            stow $1 "$i"
        else 
            echo "$i" is not valid content for $ROOT_DIR/manifest.repos
        fi
    done
}

export MANIFEST_FILE="$(pwd -P)/manifest.repos"
if [ -z "$1" ] ; then
cd $(dirname $0) 
    stow_wrapper -S

elif [ "$1" == "-D" ] ; then
    stow_wrapper -D 
fi

export MANIFEST_FILE="$(pwd -P)/manifest_disabled.repos"
stow_wrapper -D
