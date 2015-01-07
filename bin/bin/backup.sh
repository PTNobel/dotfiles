#!/bin/bash

#DEFINTIONS!
PRIMARY_DIRECTORY=/media/Toshiba_Backups
DESTINATION=${PRIMARY_DIRECTORY}/Backups
DUPLICITY_DESTINATION=file://${PRIMARY_DIRECTORY}/Duplicity
list_files() {
  \ls -a | grep -v \^$USER\$ | grep -v \^.\$ | grep -v \^..\$
}

#Check user

if [ -d "$PRIMARY_DIRECTORY/" ]; then
  if  [ -f $DESTINATION/$USER ]; then

# No files/directories should be hardcoded
    chmod -R +w $DESTINATION
    cd $DESTINATION
    rm $DESTINATION/$USER
    #ls #debug
    #file $USER  #debug
    #sleep 30 #debug
    mkdir $USER
    mv `list_files` $USER/ 
    rsync -aAv --delete --exclude=.cache $HOME $DESTINATION/
    mv $DESTINATION/$USER/* $DESTINATION
    cd $USER
    mv `list_files` $DESTINATION
    rmdir $DESTINATION/$USER
    #sleep 40 #debug
    echo $USER > $DESTINATION/$USER
    chmod -R a-w $DESTINATION
    exit $?
  else echo $DESTINATION not authorized for write by current user ; exit 2
  fi
  echo starting duplicity
  duplicity incremental --no-encryption $HOME $DUPLICITY_DESTINATION 
else echo $DESTINATION is not found ; exit 1
fi
