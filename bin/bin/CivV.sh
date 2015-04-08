#!/bin/bash
#cp $HOME/Code/core/monitors.xml.single.screen $HOME/.config/monitors.xml
#setsid gnome-shell --replace 2>/dev/null &
#echo "gnome-shell started"
25xi-layout.sh
#env DRI_PRIME=1 steam steam://rungameid/8930 &
steam steam://rungameid/8930 &
#env DRI_PRIME=1 glxinfo|grep OpenGL\ renderer
echo "steam started"
until [ "$(pidof steam | wc -w)" -ge 3 ]
do sleep 5
done
until [ "$(pidof steam | wc -w)" -le 2 ]
do sleep 30
done
#cp $HOME/Code/core/monitors.xml.dual.screen $HOME/.config/monitors.xml
#setsid gnome-shell --replace 2>/dev/null &
i3-msg restart
#sleep 3
#reload-conky.sh
exit
