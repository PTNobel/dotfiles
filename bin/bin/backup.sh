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
    mv $DESTINATION $PRIMARY_DIRECTORY/"$USER"
    chmod -R +w $PRIMARY_DIRECTORY/"$USER"
    echo pwd="$PWD"
    ls
    sh -c "rsync -apv --delete --exclude=.cache $HOME $PRIMARY_DIRECTORY ; true"
    echo "$USER" > $PRIMARY_DIRECTORY/"$USER"/"$USER"
    chmod -R a-w $PRIMARY_DIRECTORY/"$USER"
  else echo $DESTINATION not authorized for write by current user ; exit 2
  fi
  echo starting duplicity #; notify-send duplicity started
  duplicity incremental --allow-source-mismatch --no-encryption "$HOME" $DUPLICITY_DESTINATION
  mv $PRIMARY_DIRECTORY/"$USER" $DESTINATION
else echo $DESTINATION is not found ; exit 1
fi
