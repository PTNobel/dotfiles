#!/bin/bash
#
# backups the home dir to $PRIMARY_DIRECTORY/Backups

set -e
set -u

keep_computer_awake() {
  systemd-inhibit bash -c "while [[ -f /tmp/backup.lock ]] ; do sleep 60 ; done"
}

exit() {
  rm /tmp/backup.lock
  builtin exit "$@"
}
#DEFINTIONS!
PRIMARY_DIRECTORY=/media/Toshiba_Backups
PRIMARY_DIRECTORY_ntfs=/media/Toshiba_Backups_ntfs
DESTINATION=$PRIMARY_DIRECTORY_ntfs/Backups
DUPLICITY_DESTINATION=file://${PRIMARY_DIRECTORY}/Duplicity
export PRIMARY_DIRECTORY PRIMARY_DIRECTORY_ntfs DESTINATION DUPLICITY_DESTINATION

touch /tmp/backup.lock
keep_computer_awake &

backup_home() {
  # No files/directories should be hardcoded
  echo starting backup.
  sh -c "rsync -apv --delete --exclude=.cache $HOME $PRIMARY_DIRECTORY_ntfs; true"
  echo "$USER" > $PRIMARY_DIRECTORY_ntfs/"$USER"/"$USER"
}
main() {
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
    echo "Disks unmouned successfully, powering down backup drive."
    udisksctl power-off --no-user-interaction -b '/dev/disk/by-id/usb-TOSHIBA_External_USB_3.0_20140730015698-0:0' && echo "Disk powered down."
  fi
else
  echo $DESTINATION is not found ; exit 1
fi
}

main

rm /tmp/backup.lock
