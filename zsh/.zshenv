skip_global_compinit=1
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && powerline-daemon -q
if ! [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && ! [[ -z $DISPLAY && $XDG_VTNR -eq 2 ]] && [[ $- == *i* ]] && [[ -z "$TMUX" ]]; then exec tmux ; fi
