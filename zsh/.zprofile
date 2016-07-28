if [[ -z $TMUX ]]; then [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx; fi
