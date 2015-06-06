#!/bin/bash
#
# If $? at the end is 1 then the build failed.
# If $? at the end is 2 then one of the binaries referenced doesn't exist.
#

if ! [ -x update_tools_helper ] ; then
    echo Where is update_tools_helper? 1>&2
    exit 1
fi

_test(){
  while read line; do
    if ! [[ -x "$(echo "$line" | cut -f 1 -d ' ')" ]]; then
      echo can\'t find "$(echo "$line" | cut -f 1 -d ' ')" 1>&2
      exit 1
    fi
  done  < <(strings update_tools_helper | grep bin)
}

_test || exit 2
