#!/bin/bash

export OUTPUT_FILE=$(mktemp)
export ALPM_OUTPUT_FILE=$(mktemp)
#echo OUTPUT_FILE=$OUTPUT_FILE
#echo ALPM_OUTPUT_FILE=$ALPM_OUTPUT_FILE

exit_routine() {
  #echo deleting OUTPUT_FILE and WATCHDOG_FILE
  rm $OUTPUT_FILE $ALPM_OUTPUT_FILE
  exit $?
}

backup() {
  backup.sh &>> $OUTPUT_FILE || notify-send "backup.sh failed"
}

mlocate() {
  /usr/local/bin/update_tools_helper mlocate &>> $OUTPUT_FILE
}

abs_u() {
  /usr/local/bin/update_tools_helper abs &>> $OUTPUT_FILE
}

pkgfile_u() {
  /usr/local/bin/update_tools_helper pkgfile &>> $OUTPUT_FILE

}

man_u() {
  /usr/local/bin/update_tools_helper man &>> $OUTPUT_FILE
}

alpm() {
  until /usr/local/bin/update_tools_helper alpm &>> $ALPM_OUTPUT_FILE ; do sleep 1 ; done
}

yaourt_wrapper() {
  export EDITOR=vim
  yaourt "$@"
}

#TODO trap!
#trap exit_routine INT HUP TERM

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
alpm &
ALPM_PID=$!

tail -n`cat $ALPM_OUTPUT_FILE | wc -l`  -f $ALPM_OUTPUT_FILE | lolcat &

while [ -d /proc/$ALPM_PID ]; do
  sleep 1
done

echo about to launch yaourt ALPM_PID done. $ALPM_PID
yaourt_wrapper -Sua

echo "starting update of mlocate database"
mlocate &
PID[3]=$!

echo "starting update of man database"
man_u &
PID[4]=$!

yaourt_wrapper -C

tail -n`cat $OUTPUT_FILE | wc -l`  -f $OUTPUT_FILE | lolcat &

echo $PID
for i in $PID; do
  echo $i
  while [ -d /proc/$i ] ; do
    sleep 1
  done
done

echo All PIDS dead.
sleep 5
exit_routine
