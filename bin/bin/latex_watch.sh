#!/bin/bash
#
# Watches a latex file for changes and rebuilds it whenever it changes.
# Exits whenever there is no longer a .swp file.
#LATEX="$LATEX"
if [[ "$2" == "xelatex" ]]; then
  latex="xelatex  -output-directory /tmp/${USER}-LaTeX -interaction=nonstopmode"
else
  latex="pdflatex -output-directory /tmp/${USER}-LaTeX -interaction=nonstopmode"
fi
export latex
biber="biber --output-directory /tmp/${USER}-LaTeX --input-directory /tmp/${USER}-LaTeX"
export biber

function build {
  if [[ "$3" == "biber" ]]; then
    $latex "$1"
    $biber "${1%.tex}"
    $latex "$1"
  else
    $latex "$1"
    $latex "$1"
  fi
}

function check_for_changes {
  build "$1" "$2" "$3"
  while diff "$1" /tmp/"${USER}"-LaTeX/"$(basename "$1")"; do
    sleep 5
    if ! [[ -f "$(dirname "$1")"/."$(basename "$1")".swp ]]; then
      build "$1" "$2" "$3"
      exit 0
    fi
  done
  cp "$1" /tmp/"${USER}"-LaTeX/"$(basename "$1")"
  check_for_changes "$1" || exit 1
}

mkdir -p /tmp/"${USER}"-LaTeX
cp "$1" /tmp/"${USER}"-LaTeX/"$(basename "$1")"
build "$1" "$2" "$3"
rifle /tmp/"${USER}"-LaTeX/"$(basename "$1" .tex)".pdf
check_for_changes "$1" || exit 0 && exit 1
