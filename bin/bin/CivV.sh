#!/bin/bash
#cp $HOME/Code/core/monitors.xml.single.screen $HOME/.config/monitors.xml
#setsid gnome-shell --replace 2>/dev/null &
#echo "gnome-shell started"
25xi-layout.sh
#env DRI_PRIME=1 steam steam://rungameid/8930 &
steam steam://rungameid/8930 &
#env DRI_PRIME=1 glxinfo|grep OpenGL\ renderer
echo "steam started"
wait
#cp $HOME/Code/core/monitors.xml.dual.screen $HOME/.config/monitors.xml
#setsid gnome-shell --replace 2>/dev/null &
i3-msg restart
sleep 1
i3-msg restart
#sleep 3
#reload-conky.sh
exit
