#!/bin/bash

set -e
set -u

#DEFINTIONS!
PRIMARY_DIRECTORY=/media/Toshiba_Backups
DESTINATION=${PRIMARY_DIRECTORY}/Backups
DUPLICITY_DESTINATION=file://${PRIMARY_DIRECTORY}/Duplicity
list_files() {
		VAR=$(/bin/ls -a | grep -v \^$USER\$ | grep -v \^.\$ | grep -v \^..\$) #| sed s/\ /\\\ /g
  ESCAPE_KEY='\ '
  echo ${VAR// /$ESCAPE_KEY}
}

#Check user

if [ -d "$PRIMARY_DIRECTORY/" ]; then
  if [ -f $DESTINATION/$USER ]; then

# No files/directories should be hardcoded
    echo starting backup.
    chmod -R +w $DESTINATION
    #cd $DESTINATION
    #rm $DESTINATION/$USER
    #ls #debug
    #file $USER  #debug
    #sleep 30 #debug
    #mkdir $DESTINATION/$USER
	#mv $(list_files) $DESTINATION/$USER/ 
	echo pwd=$PWD
	ls
	mv $DESTINATION $PRIMARY_DIRECTORY/$USER
    bash -c "rsync -apv --delete --exclude=.cache $HOME $PRIMARY_DIRECTORY ; true"
    #mv $DESTINATION/$USER/* $DESTINATION
    mv $PRIMARY_DIRECTORY/$USER $DESTINATION
    #cd $USER
	#mv $(list_files) $DESTINATION
    #rmdir $DESTINATION/$USER
    #sleep 40 #debug
    echo $USER > $DESTINATION/$USER
    chmod -R a-w $DESTINATION
    #exit $?
  else echo $DESTINATION not authorized for write by current user ; exit 2
  fi
  echo starting duplicity #; notify-send duplicity started
  duplicity incremental --allow-source-mismatch --no-encryption $HOME $DUPLICITY_DESTINATION 
else echo $DESTINATION is not found ; exit 1
fi
