#!/bin/bash
#
# Watches a latex file for changes and rebuilds it whenever it changes.
# Exits whenever there is no longer a .swp file.
#LATEX="$LATEX"
auxdir="/tmp/${USER}-LaTeX"
latex_options="-output-directory $auxdir -interaction=nonstopmode"
if [[ "$2" ]]; then
  latex="$2 $latex_options"
else
  latex="pdflatex $latex_options"
fi
export latex
if [[ "$3" == "biber" ]]; then
biber="biber --output-directory $auxdir --input-directory $auxdir"
export biber
fi

file="$1"
export file

function build {
  if [[ "$biber" ]]; then
    $latex "$file"
    $biber "${file%.tex}"
    $latex "$file"
    cp "$auxdir"/"$(basename "${file}" .tex)".pdf ~/.latex
  else
    $latex "$file"
    $latex "$file"
    cp "$auxdir"/"$(basename "${file}" .tex)".pdf ~/.latex
  fi
}

function check_for_changes {
  build
  while diff "$file" "$auxdir"/"$(basename "$file")"; do
    sleep 5
    if ! [[ -f "$(dirname "$file")"/."$(basename "$file")".swp ]]; then
      build
      exit 0
    fi
  done
  cp "$file" "$auxdir"/"$(basename "$file")"
  check_for_changes || exit 1
}

mkdir -p "$auxdir"
cp "$file" "$auxdir"/"$(basename "$file")"
build
rifle "$auxdir"/"$(basename "${file}" .tex)".pdf
if [[ -z "$VIM" ]]; then
  check_for_changes
else
  exit 0
fi
