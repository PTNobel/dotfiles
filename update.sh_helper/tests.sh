#!/bin/bash

_test(){
for i in $(strings update_tools_helper | grep bin); do
    if echo $i | grep \- >/dev/null; then
        true
    else
        [ -x $i ] || exit 1
    fi
done
}

_test || exit 1