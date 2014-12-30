#!/bin/bash

export OUTPUT_FILE=$(mktemp)
export WATCHDOG_FILE=$(mktemp)
export PID_OF_SCRIPT=$$
#echo OUTPUT_FILE=$OUTPUT_FILE
#echo WATCHDOG_FILE=$WATCHDOG_FILE
#echo PID_OF_SCRIPT=$PID_OF_SCRIPT

#trap "exit 1" 

exit_routine() {
  echo deleting OUTPUT_FILE and WATCHDOG_FILE
  rm $OUTPUT_FILE $WATCHDOG_FILE
  echo killing script in exit_routine\(\)
  kill -s TERM $PID_OF_SCRIPT
  echo "script killed"
  exit 0
}

watchdog() {
  until [ `cat $1 | wc -l` -eq $2 ];
    do sleep 10
  done
  echo $2 processes have announced finishing: beginning shutdown routine
  exit_routine
  echo Killing
  kill -s TERM $$
}

backup() {
  backup.sh &>> $OUTPUT_FILE || notify-send "backup.sh failed"
  echo DONE >> $WATCHDOG_FILE
}

mlocate() {
  /usr/local/bin/update_tools_helper mlocate &>> $OUTPUT_FILE
  echo DONE >> $WATCHDOG_FILE
}

pkgfile_u() {
  /usr/local/bin/update_tools_helper pkgfile &>> $OUTPUT_FILE 
  echo DONE >> $WATCHDOG_FILE

}

man_u() {
  /usr/local/bin/update_tools_helper man &>> $OUTPUT_FILE
  echo DONE >> $WATCHDOG_FILE
}

watchdog $WATCHDOG_FILE 4 &

#TODO trap!
#trap exit_routine INT HUP TERM

echo "starting backup of $HOME"
backup &

setsid yaourt -S &>/dev/null &

echo "starting update of pkgfile database"
pkgfile_u &

sudo -v
yaourt -Syua

echo "starting update of mlocate database"
mlocate &

echo "starting update of man database"
man_u &

tail -n`cat $OUTPUT_FILE | wc -l`  -f $OUTPUT_FILE | lolcat
