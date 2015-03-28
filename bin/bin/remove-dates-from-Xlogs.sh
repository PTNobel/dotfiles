#!/bin/zsh
#
# Usage: $0 Xorg.*.log
# So to use this script, take a copy of Xorg.#.log (where # is a number)
# and open it in vim, possibly vi too (I haven't tested it in vi)
# and then launch this script in a different terminal, move the mouse
# over the terminal with vim and watch it work. Consider getting some tea.
#
#

export WINDOW_LOG_FILE=$(mktemp)

echo xterm -e zsh -c "echo \$WINDOWID >| $WINDOW_LOG_FILE ; vim $1" &
xterm -e zsh -c "echo \$WINDOWID >| $WINDOW_LOG_FILE ; vim $1" &
echo "$WINDOW_LOG_FILE"; cat "$WINDOW_LOG_FILE"
sleep 5
export WINDOW_ID_OF_VIM=$(cat "$WINDOW_LOG_FILE")
echo "$WINDOW_LOG_FILE"; cat "$WINDOW_LOG_FILE"
echo "$WINDOW_ID_OF_VIM"
while sleep .3; grep "^\[" "$1" >|/dev/null ; do
    echo starting a round
    xdotool key --window "$WINDOW_ID_OF_VIM" slash asciicircum backslash bracketleft Return
    xdotool key --window "$WINDOW_ID_OF_VIM" 5 d w
    xdotool key --window "$WINDOW_ID_OF_VIM" colon w Return
    exit 1
done
rm "$WINDOW_LOG_FILE"
notify-send Done\ with\ this\ file
