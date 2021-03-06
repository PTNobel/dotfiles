#!/bin/bash
#
# Partly taken from the Arch Wiki, extended by me.

function suspend_or_lock {
  if musicctl is_playing; then
    watchdog_lock "$(mktemp)" 3
  else
    lock && systemctl suspend
  fi
}

function active_lock {
  printf "Do I have write permission?\n%s\n" "$$" > "$1"
  if xrandr | grep '+' | grep '^   1366x768' >/dev/null ; then
    if xrandr | grep '+' | grep '^   1920x1080' >/dev/null ; then
      i3lock -n -d -i  "$HOME"/Pictures/noise-texture.png -t
    else
      i3lock -n -d -i "$HOME"/Pictures/262039-small.png
    fi
  else
    i3lock -n -d -i "$HOME"/Pictures/262039.png
  fi
  rm "$1"
}

function lock {
  I3LOCK_OPTIONS=-d
  export I3LOCK_OPTIONS
  generic_lock
}

function generic_lock {
  # I3LOCK_OPTIONS MUST not not be quote to insure word splitting.
  if xrandr | grep '+' | grep '^   1366x768' >/dev/null ; then
    if xrandr | grep '+' | grep '^   1920x1080' >/dev/null ; then
      i3lock $I3LOCK_OPTIONS -i  "$HOME"/Pictures/noise-texture.png -t
    else
      i3lock $I3LOCK_OPTIONS -i "$HOME"/Pictures/262039-small.png
    fi
  else
    i3lock $I3LOCK_OPTIONS -i "$HOME"/Pictures/262039.png
  fi
}

# TODO: After a computer is woken up, give the time value to unlock the
# computer and then suspend it.
function watchdog_lock {
  WATCHDOG_FILE="$1"
  NUM=0
  active_lock "$WATCHDOG_FILE" &
  while [ -f "$WATCHDOG_FILE" ] && musicctl is_playing ; do
    sleep 60s
  done
  # It needs to be sleep 60 && [ -f "$WATCHDOG_FILE" ] in order to preven the 
  # computer from suspending when it's unlooked in the last minute.
  while sleep 60s && [ -f "$WATCHDOG_FILE" ] ; do
    if [ $NUM = "$2" ]; then
      systemctl suspend && watchdog_lock "$1" "$2"
    fi
    let NUM=1+$NUM
  done
}

function generic_blur {
  file1=$(mktemp --tmpdir i3lock-wrapper-XXXXXXXXXX.png)
  file2=$(mktemp --tmpdir i3lock-wrapper-XXXXXXXXXX.png)
  scrot -zd0 "$file1"
  convert "$file1" -blur 0x9 "$file2"
  i3lock $I3LOCK_OPTIONS -i "$file2"
  trap 'rm "$file1" "$file2"' EXIT
}

function blur {
  export I3LOCK_OPTIONS
  generic_blur
}

function blur_with_sleep {
  I3LOCK_OPTIONS=-d
  export I3LOCK_OPTIONS
  generic_blur
}

function freeze {
  file1=$(mktemp --tmpdir i3lock-wrapper-XXXXXXXXXX.png)
  scrot -d1 -z "$file1"
  i3lock -i "$file1"
  trap 'rm "$file1"' EXIT
}

function usage {
  echo "Usage: $0 OPTION"
  echo "OPTIONS:"
  echo "  lock - Locks screen and turns off the monitor. (depends on i3lock)"
  echo "  inactive_lock - lock, but suspends computer after 30 minutes (depends on i3lock and systemctl)"
  echo "  short_inactive_lock - inactive_lock, but 3m"
  echo "  lock_without_sleep - locks screen but leaves the screen on (depends on i3lock)"
  echo "  blur - blurs screen (depends on scrot, convert [from imagemagick], and i3lock)"
  echo "  blur_with_sleep - blur, but turns off  the monitor. (depends on scrot, convert [from imagemagick], and i3lock)"
  echo "  freeze - freezes the screen (depends on scrot and i3lock)"
  echo "  suspend_or_lock - suspend the computer if music is not being played, otherwise lock it. (depends on musicctl is_playing)"
  echo "  logout - exits i3 (depends on i3-msg)"
  echo "  suspend - locks screen and suspends the computer (depends on i3lock and systemctl)"
  echo "  hibernate - locks screen and hibernates the computer (depends on i3lock and systemctl)"
  echo "  reboot - reboots (depends on systemctl)"
  echo "  shutdown - shutsdown (depends on systemctl)"
  echo "  usage - print this help and exit"
  echo "  help - print this help and exit"
}

case "$1" in
  lock)
    lock
    ;;
  lock_without_sleep)
    export I3LOCK_OPTIONS
    generic_lock
    ;;
  blur)
    blur
    ;;
  blur_with_sleep)
    blur_with_sleep
    ;;
  freeze)
    freeze
    ;;
  logout)
    i3-msg exit
    ;;
  suspend)
    lock && systemctl suspend
    ;;
  hibernate)
    lock && systemctl hibernate
    ;;
  reboot)
    systemctl reboot
    ;;
  shutdown)
    systemctl poweroff
    ;;
  short_inactive_lock)
    watchdog_lock "$(mktemp)" 3
    ;;
  inactive_lock)
    watchdog_lock "$(mktemp)" 15
    ;;
  watchdog_lock)
    watchdog_lock "$2" "$3"
    ;;
  suspend_or_lock)
    suspend_or_lock
    ;;
  usage|help|-h|--help)
    usage
    ;;
  "")
    usage
    exit 3
    ;;
  *)
    echo "Invalid arguement"
    usage
    exit 2
esac

exit 0
