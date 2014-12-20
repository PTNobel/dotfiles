#!/bin/bash

export OUTPUT_FILE=$(mktemp)
export WATCHDOG_FILE=$(mktemp)

#echo OUTPUT_FILE=$OUTPUT_FILE
#echo WATCHDOG_FILE=$WATCHDOG_FILE

exit_routine() {
  echo deleting OUTPUT_FILE and WATCHDOG_FILE
  rm $OUTPUT_FILE $WATCHDOG_FILE
  echo killing script
  trap - HUP INT TERM
  kill $$
  exit 0
}

watchdog() {
  until [ `cat $1 | wc -l` -eq $2 ];
    do sleep 10
  done
  echo $2 processes have announced finishing: beginning shutdown routine
  exit_routine
  echo Killing
  kill $$
}

backup() {
  backup.sh &>> $OUTPUT_FILE || notify-send "backup.sh failed"
  echo DONE >> $WATCHDOG_FILE
}

#TODO: Handle already locked mlocate.db: Draft implemented 
mlocate() {
  until sudo -E updatedb &>> $OUTPUT_FILE
  do sleep 30
  done
  echo DONE >> $WATCHDOG_FILE
}

pkgfile_u() {
  sudo -E pkgfile -u &>> $OUTPUT_FILE 
  echo DONE >> $WATCHDOG_FILE

}

man_u() {
  sudo -E mandb &>> $OUTPUT_FILE 
  echo DONE >> $WATCHDOG_FILE
}

watchdog $WATCHDOG_FILE 5 &

#TODO trap!
#trap exit_routine INT HUP TERM

echo "starting backup of $HOME"
backup &

setsid yaourt -S &>/dev/null &

sudo -v

echo "starting update of mlocate database"
mlocate &

echo "starting update of pkgfile database"
pkgfile_u &

yaourt -Syua

sudo -v

echo "starting update of mlocate database"
mlocate &

echo "starting update of man database"
man_u &

tail -n`cat $OUTPUT_FILE | wc -l`  -f $OUTPUT_FILE | lolcat
