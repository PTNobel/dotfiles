#!/bin/bash
#
# Watches a latex file for changes and rebuilds it whenever it changes.
# Exits whenever there is no longer a .swp file.
LATEX="$LATEX"

if [ -z "$LATEX" ] ; then latex="$LATEX"; else
  latex="pdflatex -interaction=nonstopmode -output-directory /tmp"
  #latex="xelatex -interaction=nonstopmode -output-directory /tmp"
fi
export latex

check_for_changes() {
  $latex "$1"
  while diff "$1" /tmp/"$(basename "$1")"; do
    sleep 5
    if ! [[ -f "$(dirname "$1")"/."$(basename "$1")".swp ]]; then
      $latex "$1"
      $latex "$1"
      exit 0
    fi
  done
  #$latex "$1"
  cp "$1" /tmp/"$(basename "$1")"
  check_for_changes "$1" || exit 1
}

cp "$1" /tmp/"$(basename "$1")"
$latex "$1"
check_for_changes "$1" || exit 0 && exit 1
