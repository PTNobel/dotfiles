#!/bin/bash
#
# backups the home dir to $PRIMARY_DIRECTORY/Backups

set -e
set -u

#DEFINTIONS!
PRIMARY_DIRECTORY=/media/Toshiba_Backups
PRIMARY_DIRECTORY_ntfs=/media/Toshiba_Backups_ntfs
DESTINATION=$PRIMARY_DIRECTORY_ntfs/Backups
DUPLICITY_DESTINATION=file://${PRIMARY_DIRECTORY}/Duplicity
export PRIMARY_DIRECTORY PRIMARY_DIRECTORY_ntfs DESTINATION DUPLICITY_DESTINATION

backup_home() {
  # No files/directories should be hardcoded
  echo starting backup.
  sh -c "rsync -apv --delete --exclude=.cache $HOME $PRIMARY_DIRECTORY_ntfs; true"
  echo "$USER" > $PRIMARY_DIRECTORY_ntfs/"$USER"/"$USER"
}

if [ -d "$PRIMARY_DIRECTORY/" ]; then
  if [ -f $DESTINATION/"$USER" ]; then
    mv $DESTINATION $PRIMARY_DIRECTORY_ntfs/"$USER"
    backup_home &

  else
    echo $DESTINATION not authorized for write by current user ; exit 2
  fi

  echo starting duplicity #; notify-send duplicity started
  bash -c 'duplicity incremental --allow-source-mismatch --no-encryption "$HOME" $DUPLICITY_DESTINATION ; true' &
  wait
  mv $PRIMARY_DIRECTORY_ntfs/"$USER" $DESTINATION
  # Cleaning up.
  cd /media
  if udevil umount $PRIMARY_DIRECTORY && udevil umount $PRIMARY_DIRECTORY_ntfs; then
    udisksctl power-off --no-user-interaction -b '/dev/disk/by-id/usb-TOSHIBA_External_USB_3.0_20140730015698-0:0'
  fi
else
  echo $DESTINATION is not found ; exit 1
fi
