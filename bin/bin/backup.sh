#!/bin/bash

#DEFINTIONS!
DESTINATION=/media/Toshiba_Backups
list_files() {
  \ls -a | grep -v \^$USER\$ | grep -v \^.\$ | grep -v \^..\$
}

#Check user

if  [ -f $DESTINATION/$USER ]; then

# No files/directories should be hardcoded
  if [ -d "$DESTINATION/" ]; then
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
  else echo $DESTINATION is not found ; exit 1
  fi

else echo $DESTINATION not authorized for write by current user ; exit 10
fi
