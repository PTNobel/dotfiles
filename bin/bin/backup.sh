#!/bin/bash
DESTINATION=/media/Toshiba_Backups
list_files() {
  \ls -a | grep -v \^$USER\$ | grep -v \^.\$ | grep -v \^..\$
}
if [ -d "$DESTINATION/" ]; then
  cd $DESTINATION
  mkdir $USER
  mv `list_files` $USER/ 
  rsync -aAv --delete --exclude=.cache $HOME $DESTINATION/
  rsync -aAv --delete $HOME/.dotfiles/* $DESTINATION/$USER/.dotfiles/
  mv $DESTINATION/$USER/* $DESTINATION
  cd $USER
  mv `list_files` $DESTINATION
  rmdir $DESTINATION/$USER
  exit $?
else echo $DESTINATION is not found ; exit 1
fi
