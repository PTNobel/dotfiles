#!/bin/bash
#
# Watches a latex file for changes and rebuilds it whenever it changes.
# Exits whenever there is no longer a .swp file.

latex="pdflatex -interaction=batchmode"
export latex

check_for_changes() {
  while diff "$1" /tmp/"$(basename "$1")"; do
    sleep 10
    if ! [[ -f "$(dirname "$1")"/."$(basename "$1")".swp ]]; then
      exit 0

    fi
  done

  $latex "$1"
  cp "$1" /tmp/"$(basename "$1")"
  check_for_changes "$1" || exit 1
}

cp "$1" /tmp/"$(basename "$1")"
$latex "$1"
check_for_changes "$1" || exit 0 && exit 1
