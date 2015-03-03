#!/bin/bash

stow_wrapper(){
    for i in $(cat "$MANIFEST_FILE"); do
        if [ -d $i ] || true ; then
            #echo $i $1
            echo stow $1 "$i"
            stow $1 "$i"
        else 
            echo "$i" is not valid content for $MANIFEST_FILE
        fi
    done
}

cd $(dirname $0) 

export MANIFEST_FILE="$(pwd -P)/manifest.repos"
if [ -z "$1" ] ; then
    stow_wrapper -R

elif [ "$1" == "-D" ] ; then
    stow_wrapper -D 
fi

export MANIFEST_FILE="$(pwd -P)/manifest_disabled.repos"
stow_wrapper -D

for i in $(cat $(pwd -P)/manifest_build.repos); do
    cd $i
    make || exit 1
    make test || exit 1
    sudo make install || exit 1
    make clean || exit 1
    cd $(dirname $0) 
done
