#!/bin/bash
#
# Updates my system.

if [[ -f /tmp/update.lock ]] ; then exit ; else touch /tmp/update.lock ; fi

OUTPUT_FILE=$(mktemp)
export OUTPUT_FILE
#echo OUTPUT_FILE=$OUTPUT_FILE

keep_computer_awake() {
  systemd-inhibit bash -c "while [[ -f $OUTPUT_FILE ]] ; do sleep 60 ; done"
}

exit_routine() {
  #echo deleting OUTPUT_FILE and WATCHDOG_FILE
  rm "$OUTPUT_FILE" /tmp/update.lock
  exit $?
}

backup() {
  backup.sh &>> "$OUTPUT_FILE" || notify-send "backup.sh failed"
}

mlocate() {
  /usr/local/bin/update_tools_helper mlocate &>> "$OUTPUT_FILE"
}

abs_u() {
  /usr/local/bin/update_tools_helper abs &>> "$OUTPUT_FILE"
}

pkgfile_u() {
  /usr/local/bin/update_tools_helper pkgfile &>> "$OUTPUT_FILE"

}

man_u() {
  /usr/local/bin/update_tools_helper man &>> "$OUTPUT_FILE"
}

units_cur_u() {
  /usr/local/bin/update_tools_helper units &>> "$OUTPUT_FILE"
}

alpm() {
  until /usr/local/bin/update_tools_helper alpm ; do sleep 1 ; done
}

yaourt_wrapper() {
  export EDITOR=vim
  yaourt "$@"
}

keep_computer_awake &

echo "starting backup of $HOME"
backup &
PID1=$!

setsid yaourt -S &>/dev/null

echo "starting update of pkgfile database"
pkgfile_u &
PID2=$!

echo "starting update of abs database"
abs_u &
PID3=$!

echo "starting update of alpm database"
alpm

yaourt_wrapper -Sua
PID4=$!

echo "starting update of mlocate database"
mlocate &
PID5=$!

echo "starting update of man database"
man_u &
PID6=$!

echo "starting update of units database"
units_cur_u &
PID7=$!

yaourt_wrapper -C
PID8=$!

tail -n"$( wc -l < "$OUTPUT_FILE")"  -f "$OUTPUT_FILE" | lolcat &

wait $PID1 $PID2 $PID3 $PID4 $PID5 $PID6 $PID7 $PID8
exit_routine
