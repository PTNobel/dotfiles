#!/bin/bash
#
# backups the home dir to $PRIMARY_DIRECTORY/Backups

set -e
set -u

#DEFINTIONS!
PRIMARY_DIRECTORY=/media/Toshiba_Backups
DESTINATION=${PRIMARY_DIRECTORY}/Backups
DUPLICITY_DESTINATION=file://${PRIMARY_DIRECTORY}/Duplicity

if [ -d "$PRIMARY_DIRECTORY/" ]; then
  if [ -f $DESTINATION/"$USER" ]; then

# No files/directories should be hardcoded
    echo starting backup.
    chmod -R +w $DESTINATION
    echo pwd="$PWD"
    ls
    mv $DESTINATION $PRIMARY_DIRECTORY/"$USER"
    sh -c "rsync -apv --delete --exclude=.cache $HOME $PRIMARY_DIRECTORY ; true"
    mv $PRIMARY_DIRECTORY/"$USER" $DESTINATION
    echo "$USER" > $DESTINATION/"$USER"
    chmod -R a-w $DESTINATION
  else echo $DESTINATION not authorized for write by current user ; exit 2
  fi
  echo starting duplicity #; notify-send duplicity started
  duplicity incremental --allow-source-mismatch --no-encryption "$HOME" $DUPLICITY_DESTINATION
else echo $DESTINATION is not found ; exit 1
fi
