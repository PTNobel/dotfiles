#!/bin/bash
#
# If $? at the end is 1 then the build failed.
# If $? at the end is 2 then one of the binaries referenced doesn't exist.
#

[ -x update_tools_helper ] || echo Where is update_tools_helper? 1>&2
[ -x update_tools_helper ] || exit 1

_test(){
for i in $(strings update_tools_helper | grep bin); do
    if echo $i | grep \- >/dev/null; then
        true
    else
        [ -x $i ] || echo can\'t find $i. 1>&2
        [ -x $i ] || exit 1
    fi
done
}

_test || exit 2
