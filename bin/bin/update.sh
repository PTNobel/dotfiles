#!/bin/bash

export OUTPUT_FILE=$(mktemp)
#echo OUTPUT_FILE=$OUTPUT_FILE

exit_routine() {
  #echo deleting OUTPUT_FILE and WATCHDOG_FILE
  rm "$OUTPUT_FILE"
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

alpm() {
  until /usr/local/bin/update_tools_helper alpm ; do sleep 1 ; done
}

yaourt_wrapper() {
  export EDITOR=vim
  yaourt "$@"
}


echo "starting backup of $HOME"
backup &
PID[1]=$!

setsid yaourt -S &>/dev/null &

echo "starting update of pkgfile database"
pkgfile_u &
PID[2]=$!

echo "starting update of abs database"
abs_u &
PID[5]=$!

echo "starting update of alpm database"
alpm

yaourt_wrapper -Sua

echo "starting update of mlocate database"
mlocate &
PID[3]=$!

echo "starting update of man database"
man_u &
PID[4]=$!

yaourt_wrapper -C

tail -n"$( wc -l < "$OUTPUT_FILE")"  -f "$OUTPUT_FILE" | lolcat &

echo "$PID"
for i in $PID; do
  echo "$i"
  while [ -d /proc/"$i" ] ; do
    sleep 1
  done
done

echo All PIDS dead.
sleep 5
exit_routine
