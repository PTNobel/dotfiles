#!/bin/bash

sudo -v

yaourt -Syua

OUTPUT_FILE=$(mktemp)

sudo -v

echo "starting update of pkgfile database"
sudo pkgfile -u &>>$OUTPUT_FILE &
echo "starting update of mlocate database"
sudo updatedb & &>>$OUTPUT_FILE &
echo "starting update of man database"
sudo mandb &>>$OUTPUT_FILE &
echo "starting backup of $USER home directory"
backup.sh &>>$OUTPUT_FILE &
tail -f $OUTPUT_FILE | lolcat
