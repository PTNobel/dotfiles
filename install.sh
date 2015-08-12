#!/bin/bash

stow_wrapper(){
  for i in $(cat "$MANIFEST_FILE"); do
    if [ -d "$i" ] || true ; then
      #echo $i $1
      echo stow "$1" "$i"
      stow "$1" "$i"
    else
      echo "$i" is not valid content for "$MANIFEST_FILE"
    fi
  done
}

cd "$(dirname "$0")"

MANIFEST_FILE="$(pwd -P)/manifest.repos"
export MANIFEST_FILE
if [ "$1" == "-D" ] ; then
  stow_wrapper -D
  exit 1
elif [ -z "$1" ] ; then
  stow_wrapper -R
else
  echo What was that option you passed me?
  exit 3
fi

MANIFEST_FILE="$(pwd -P)/manifest_disabled.repos"
export MANIFEST_FILE
stow_wrapper -D

for i in $(cat "$(pwd -P)"/manifest_build.repos); do
  cd "$i"
  make || exit 1
  make test || exit 1
  sudo make install || exit 1
  make clean || exit 1
  cd ..
done

for i in $(cat "$(pwd -P)"/manifest_usr_local.files); do
  sudo cp "$i" /usr/local/bin/
done
