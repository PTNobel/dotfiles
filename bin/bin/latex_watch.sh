#!/bin/bash
#
# Watches a latex file for changes and rebuilds it whenever it changes.
# Exits whenever there is no longer a .swp file.
#LATEX="$LATEX"
if [ "$2" == "xelatex" ]; then
  latex="xelatex  -output-directory /tmp/${USER}-LaTeX -interaction=nonstopmode"
else
  latex="pdflatex -output-directory /tmp/${USER}-LaTeX -interaction=nonstopmode"
fi
export latex

function check_for_changes {
  $latex "$1"
  while diff "$1" /tmp/"${USER}"-LaTeX/"$(basename "$1")"; do
    sleep 5
    if ! [[ -f "$(dirname "$1")"/."$(basename "$1")".swp ]]; then
      $latex "$1"
      $latex "$1"
      exit 0
    fi
  done
  #$latex "$1"
  cp "$1" /tmp/"${USER}"-LaTeX/"$(basename "$1")"
  check_for_changes "$1" || exit 1
}

mkdir -p /tmp/"${USER}"-LaTeX
cp "$1" /tmp/"${USER}"-LaTeX/"$(basename "$1")"
$latex "$1"
rifle /tmp/"${USER}"-LaTeX/"$(basename "$1" .tex)".pdf
check_for_changes "$1" || exit 0 && exit 1
