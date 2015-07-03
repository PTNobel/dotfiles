skip_global_compinit=1
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && source /etc/profile && exec startx
[[ $- == *i* ]] && [[ -z "$TMUX" ]] && exec tmux
