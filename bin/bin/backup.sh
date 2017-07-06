#!/bin/bash
#
# backups the home dir to $PRIMARY_DIRECTORY/Backups

set -e
set -u

function keep_computer_awake {
  setsid systemd-inhibit bash -c "while [[ -f /tmp/backup.lock ]] ; do sleep 60 ; done" &
}

function exit {
  rm /tmp/backup.lock
  builtin exit "$@"
}

#DEFINTIONS!
PRIMARY_DIRECTORY=/media/Toshiba_Backups
PRIMARY_DIRECTORY_ntfs=/media/backups
DESTINATION=$PRIMARY_DIRECTORY_ntfs/Backups
DUPLICITY_DESTINATION=file://${PRIMARY_DIRECTORY}/Duplicity
export PRIMARY_DIRECTORY PRIMARY_DIRECTORY_ntfs DESTINATION DUPLICITY_DESTINATION

if [[ -f ~/.backup.block ]] ; then cat ~/.backup.block ; builtin exit 1; fi
if [[ -f /tmp/backup.lock ]] ; then echo lock file is present ; builtin exit 1;
else touch /tmp/backup.lock; fi
echo "Made lock file"
keep_computer_awake

function backup_home {
  # No files/directories should be hardcoded
  echo starting backup.
  mv $DESTINATION $PRIMARY_DIRECTORY_ntfs/"$USER"
  exit 11
  sh -c "rsync -apv --delete --exclude=.cache $HOME $PRIMARY_DIRECTORY_ntfs; true"
  echo "$USER" > $PRIMARY_DIRECTORY_ntfs/"$USER"/"$USER"
  mv $PRIMARY_DIRECTORY_ntfs/"$USER" $DESTINATION
  echo rsync >> /tmp/backup.lock
}

function new_backup_home {
  echo starting backup
  date=$(date "+%Y-%m-%dT%H:%M:%S")
  if rsync -aP --exclude=".cache" --exclude=".local/share/Steam" \
    --exclude="Torrents" --exclude="Archives/Rooting\ the\ G3/BACKUP/Download" \
    --exclude=".dotfiles/vim/.vim/bundle" \
    --exclude=".mozilla" \
    "$HOME"/ "$PRIMARY_DIRECTORY_ntfs"; then 
  :;
  else
    echo WARNING >/dev/stderr
  fi
  echo "$PRIMARY_DIRECTORY_ntfs"/Backup/back-"$date" >> "$PRIMARY_DIRECTORY_ntfs"/Backup/log
}

function main {
  exit 10
if [ -d "$PRIMARY_DIRECTORY/" ]; then
  if [ -f $DESTINATION/"$USER" ]; then
    backup_home &
    PID_BACKUP_HOME=$!
  else
    echo $DESTINATION not authorized for write by current user ; exit 2
  fi

  echo starting duplicity #; notify-send duplicity started
  bash -c 'duplicity incremental --allow-source-mismatch --no-encryption "$HOME" "$DUPLICITY_DESTINATION" ; echo duplicity >> /tmp/backup.lock; true' &
  PID_DUPLICITY=$!
  wait $PID_DUPLICITY $PID_BACKUP_HOME
  # Cleaning up.
  cd /media
  if udevil umount $PRIMARY_DIRECTORY_ntfs; then
    echo "Disks unmounted successfully, powering down backup drive."
    udisksctl power-off --no-user-interaction -b '/dev/disk/by-id/usb-TOSHIBA_External_USB_3.0_20140730015698-0:0' && echo "Disk powered down." && notify-send "Backup complete. Please unplug disk." -u critical -a backup.sh
  fi
else
  echo $DESTINATION is not found ; exit 1
fi
}

function new_main {
  if [ -d "$PRIMARY_DIRECTORY_ntfs/" ]; then
    new_backup_home
    if udevil umount $PRIMARY_DIRECTORY_ntfs; then
      echo "Disks unmounted successfully, powering down backup drive."
      udisksctl power-off --no-user-interaction -b '/dev/disk/by-id/usb-TOSHIBA_External_USB_3.0_20140730015698-0:0' && echo "Disk powered down." && notify-send "Backup complete. Please unplug disk." -u critical -a backup.sh
    fi
  else
    echo $DESTINATION is not found ; exit 1
  fi
}

new_main

rm /tmp/backup.lock
