#!/usr/bin/python3
#
# Partly taken from the Arch Wiki, extended by me.

import os
import sys
import time
import subprocess
import player


def suspend_or_lock():
    if player.is_playing():
        watchdog_lock(3)
    else:
        lock()
        suspend()


def lock():
    generic_lock(['-d'])


def generic_lock(i3LockOptions=[]):
    subprocess.call(['i3lock'] + i3LockOptions + ['-t', '-i', which_picture()])


def which_picture():
    xrandr_output = subprocess.check_output(['xrandr']).split(b'\n')
    active_output = list()
    HDMI_active = bool()
    LVDS_active = bool()
    for i in xrandr_output:
        if b'+' in i and b'connected' in i:
            active_output.append(i)

    for i in active_output:
        if b'LVDS' in i:
            LVDS_active = True

        elif b'HDMI' in i:
            HDMI_active = True

    if HDMI_active and LVDS_active:
        output = os.path.expanduser("~/Pictures/noise-texture.png")
    elif HDMI_active and not LVDS_active:
        output = os.path.expanduser("~/Pictures/262039.png")
    else:
        output = os.path.expanduser("~/Pictures/262039-small.png")

    return output


def watchdog_lock(wait_time):
    i3lock = subprocess.Popen(['i3lock', '-n', '-d'] +
                              ['-t', '-i', which_picture()])
    counter = int()
    # i3lock.poll() is used, instead of i3lock.returncode, in order to prevent
    # i3lock from becoming a zombie, which would never be reaped.
    while i3lock.poll() is None:
        if counter < wait_time:
            counter += 1
        elif player.is_playing():
            pass
        else:
            suspend()
        # time.sleep() is placed here in order to prevent the screen from being
        # lockerevent the screen from being
        # locked if it's unlocked in the last minute.
        time.sleep(60)


def inactive_lock():
    watchdog_lock(15)


def short_inactive_lock():
    watchdog_lock(3)


def suspend():
    lock()
    subprocess.call(['systemctl', 'suspend'])


def generic_blur(i3LockOptions):
    fileName1 = str(subprocess.Popen(
                    ['mktemp', '--tmpdir',
                     'i3lock-wrapper-XXXXXXX.png'],
                    stdout=subprocess.PIPE).communicate()[0].strip())[2:-1]
    fileName2 = str(subprocess.Popen(
                    ['mktemp', '--tmpdir',
                     'i3lock-wrapper-XXXXXXX.png'],
                    stdout=subprocess.PIPE).communicate()[0].strip())[2:-1]
    try:
        subprocess.call(['scrot', '-zd0', fileName1])
        subprocess.call(['convert', fileName1, '-blur', '0x9', fileName2])
        subprocess.call(['i3lock'] + i3LockOptions + ['-i', fileName2])
        raise
    except:
        subprocess.call(['rm', fileName1, fileName2])


def blur():
    generic_blur([])


def blur_with_sleep():
    generic_blur(['-d'])


def freeze():
    fileName1 = str(subprocess.Popen(
                    ['mktemp', '--tmpdir',
                     'i3lock-wrapper-XXXXXXX.png'],
                    stdout=subprocess.PIPE).communicate()[0].strip())[2:-1]
    try:
        subprocess.call(['scrot', '-zd0', fileName1])
        subprocess.call(['i3lock', '-i', fileName1])
        raise
    except:
        subprocess.call(['rm', fileName1])


def logout():
    subprocess.call(['i3-msg', 'exit'])


def hibernate():
    lock()
    subprocess.call(['systemctl', 'hibernate'])


def reboot():
    subprocess.call(['systemctl', 'reboot'])


def shutdown():
    subprocess.call(['systemctl', 'poweroff'])


def usage():
    print('Usage: i3exit <option>')
    print('Options:')
    for i in option_dict.keys():
        print('\t' + i)
    pass


def log():
    import datetime
    fd = open(os.path.expanduser('~/.i3exit.log'), mode='a')
    fd.write(str({'date': datetime.datetime.now(), 'argv': sys.argv}))
    fd.write('\n')
    fd.close()


option_dict = {'lock': lock,
               'lock_without_sleep': generic_lock,
               'inactive_lock': inactive_lock,
               'short_inactive_lock': short_inactive_lock,
               'suspend_or_lock': suspend_or_lock,
               'blur': blur,
               'blur_with_sleep': blur_with_sleep,
               'freeze': freeze,
               'logout': logout,
               'suspend': suspend,
               'hibernate': hibernate,
               'reboot': reboot,
               'shutdown': shutdown,
               'usage': usage,
               }


if __name__ == '__main__':
    try:
        option_dict[sys.argv[1]]()
        log()
    except (IndexError, KeyError):
        usage()
        log()
        exit(1)
