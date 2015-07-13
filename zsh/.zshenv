skip_global_compinit=1
#[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && source /etc/profile && exec startx
if ! [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && [[ $- == *i* ]] && [[ -z "$TMUX" ]] then exec tmux ; fi
