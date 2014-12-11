#!/bin/bash

export OUTPUT_FILE=$(mktemp)
export WATCHDOG_FILE=$(mktemp)

#echo OUTPUT_FILE=$OUTPUT_FILE
#echo WATCHDOG_FILE=$WATCHDOG_FILE

watchdog() {
  until [ `cat $1 | wc -l` -eq 4 ];
    do sleep 10
  done
  echo 4 processes have announced finishing: beginning shutdown routine
  echo deleting OUTPUT_FILE and WATCHDOG_FILE
  rm $OUTPUT_FILE $WATCHDOG_FILE
  echo killing script 
  sleep 3
  kill $$
}

watchdog $WATCHDOG_FILE &

sudo -v


echo "starting update of pkgfile database"
sudo -E bash -c 'pkgfile -u &>> $OUTPUT_FILE ; echo DONE >> $WATCHDOG_FILE' &

echo "starting backup of $USER home directory"
bash -c 'backup.sh &>> $OUTPUT_FILE ; echo DONE >> $WATCHDOG_FILE' &

yaourt -Syua


sudo -v

echo "starting update of mlocate database"
sudo -E bash -c 'updatedb &>> $OUTPUT_FILE ; echo DONE >> $WATCHDOG_FILE' &
echo "starting update of man database"
sudo -E bash -c 'mandb &>> $OUTPUT_FILE ; echo DONE >> $WATCHDOG_FILE' &
tail -f $OUTPUT_FILE | lolcat
