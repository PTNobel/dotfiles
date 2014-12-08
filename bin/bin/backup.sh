#!/bin/bash
DESTINATION=/media/Toshiba_Backups
if [ -d "$DESTINATION/" ]; then
  #mv `\ls -a | grep -v \^$USER\$ | grep -v \^.\$ | grep -v \^..\$` $USER/
  rsync -aAv --delete --exclude=.cache $HOME $DESTINATION/
  rsync -aAv --delete --exlude=.cache $HOME/.* $DESTINATION/$USER/
  rsync -aAv --delete $HOME/.dotfiles/* $DESTINATION/$USER/.dotfiles/
  #mv $DESTINATION/$USER/* $DESTINATION
  #mv $DESTINATION/$USER/.* $DESTINATION
  #rmdir $DESTINATION/$USER
else echo $DESTINATION is not found ; exit 1
fi
