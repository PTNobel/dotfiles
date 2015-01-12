#!/bin/bash

echo '#TODO xrandr -q
if xrandr --output HDMI1 --mode 1920x1080 --pos 1366x0 --rotate normal --primary; then
    xrandr --output LVDS1 --mode 1366x768 --pos 0x809 --rotate normal
else
    xrandr --output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal --primary ; xrandr --output HDMI1 --off
fi
xrandr --output VIRTUAL1 --off
xrandr --output DP1 --off
xrandr --output VGA1 --off
xrandr --setprovideroffloadsink radeon Intel' >/dev/null
#!/bin/bash

kill `pidof -x $0 -o %PPID`

# default monitor is LVDS1
MONITOR=LVDS1

# functions to switch from LVDS1 to HDMI and vice versa
function ActivateHDMI {
    echo "Switching to HDMI1"
    xrandr --output HDMI1 --mode 1920x1080 --pos 1366x0 --rotate normal --primary
	xrandr --output LVDS1 --mode 1366x768  --pos 0x809  --rotate normal
	sh $HOME/.fehbg
    MONITOR=HDMI1
}
function DeactivateHDMI {
    echo "Switching to LVDS1"
    xrandr --output HDMI1 --off
	xrandr --output LVDS1 --mode 1366-768  --pos 0x0    --rotate normal --primary 
    MONITOR=LVDS1
	sh $HOME/.fehbg
}

# functions to check if HDMI is connected and in use
function HDMIActive {
    [ $MONITOR = "HDMI1" ]
}
function HDMIConnected {
    ! xrandr | grep "^HDMI1" | grep disconnected >/dev/null
}

xrandr --output VIRTUAL1 --off
xrandr --output DP1 --off
xrandr --output VGA1 --off
xrandr --setprovideroffloadsink radeon Intel

# actual script
while true; do

    if ! HDMIActive && HDMIConnected; then
        ActivateHDMI

    elif HDMIActive && ! HDMIConnected; then
        DeactivateHDMI

    fi

    sleep 1s
done
