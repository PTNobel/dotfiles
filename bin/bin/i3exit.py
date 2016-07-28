#!/usr/bin/env python3


import os
import sys
import time
import subprocess
import player
from typing import Tuple


def generic_lock(i3LockOptions=[]) -> subprocess.Popen:
    return plain_lock(i3LockOptions + ['-i' + _which_picture()])


def plain_lock(i3LockOptions=[]) -> subprocess.Popen:
    return subprocess.Popen(['i3lock'] + i3LockOptions + ['-t'])


def which_output() -> Tuple[bool, bool]:
    """returns tuple of LVDS_active bool and HDMI_active bool"""
    xrandr_output = subprocess.check_output(['xrandr']).split(b'\n')
    active_outputs = list()
    HDMI_active = bool()
    LVDS_active = bool()
    for line in xrandr_output:
        if b'+' in line and b'connected' in line:
            active_outputs.append(line)

    for output in active_outputs:
        if b'LVDS' in output:
            LVDS_active = True

        elif b'HDMI' in output:
            HDMI_active = True

    return (LVDS_active, HDMI_active)


def _which_picture() -> str:
    LVDS_active, HDMI_active = which_output()
    if HDMI_active and LVDS_active:
        output = os.path.expanduser("~/Pictures/noise-texture.png")
    elif HDMI_active and not LVDS_active:
        output = os.path.expanduser("~/Pictures/262039.png")
    else:
        output = os.path.expanduser("~/Pictures/262039-small.png")

    return output


def watchdog_lock_wrapper():
    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        watchdog_lock(int(sys.argv[2]))
    else:
        exit(1)


def watchdog_lock(wait_time,  sleep_for=60, generic_locker=generic_lock):
    i3lock = generic_locker(['-n', '-d'])
    counter = int()
    # i3lock.poll() is used, instead of i3lock.returncode, in order to prevent
    # i3lock from becoming a zombie, which would never be reaped.
    while i3lock.poll() is None:
        if counter < wait_time:
            counter += 1
        elif player.is_playing():
            pass
        # The second i3lock check is for the edgecase where when
        # player.is_playing() takes 2 seconds (which can happen in
        # player.pianobar.is_playing()) and the screen is unlocked in that
        # time.
        elif i3lock.poll() is None:
            suspend()
        # time.sleep() is placed here in order to prevent the computer from
        # being suspended if it's unlocked in the last sleep_for seconds.
        time.sleep(sleep_for)


def suspend(lockScreen=False):
    if lockScreen:
        generic_lock(['-d'])

    # SUSPEND IS DISABLED IF IT'S RUNNING ON A KERNEL KNOWN TO HAVE SUSPEND
    # ISSUES
    if '4.5.0-1-ARCH' in subprocess.getoutput(['uname', '-r']):
        print("WARNING: SUSPEND IS KNOWN TO NOT WORK WITH THIS KERNEL",
              file=sys.stderr)
        exit(200)
    else:
        subprocess.call(['systemctl', 'suspend'])


def generic_blur(i3LockOptions=[]):
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


def hibernate():
    generic_lock(['-d'])
    subprocess.call(['systemctl', 'hibernate'])


def _log():
    import datetime
    fd = open(os.path.expanduser('~/.i3exit.log'), mode='a')
    fd.write(str({'date': datetime.datetime.now(), 'argv': sys.argv}))
    fd.write('\n')
    fd.close()


def main():
    def usage():
        print('Usage: ' + arguments['name'] + ' <option>')
        print('Options:')
        for i in option_dict.keys():
            print('\t' + i)

    def processargs():
        # All of these run in the same scope as processargs(). They make changes
        # to output.
        def _help():
            output['usage'] = 'help'

        # In place of a switch-case statement the following dictionaires link
        # argv entries to functions.
        long_args_to_disc = {'--help': _help}
        short_args_to_disc = {'h': _help}
        output = {
            "input": str(),
            "name": os.path.basename(sys.argv[0]),
            }
        indexes_to_ignore = list()

        if len(sys.argv) == 1:
            exit(1)
        else:
            # range() starts at 1 to prevent the name from being processed.
            for i in range(1, len(sys.argv)):
                if i in indexes_to_ignore:
                    continue

                elif len(sys.argv[i]) >= 2 and sys.argv[i][0:2] == '--':
                    try:
                        long_args_to_disc[sys.argv[i].split('=')[0]]()
                    except KeyError:
                        exit(1)

                elif sys.argv[i][0] == '-' and sys.argv[i][1] != '-':
                    for j in range(1, len(sys.argv[i])):
                        try:
                            short_args_to_disc[sys.argv[i][j]]()
                        except KeyError:
                            exit(1)

                elif not output["input"]:
                    output["input"] = sys.argv[i]

        return output

    arguments = processargs()

    try:
        option_dict = {'lock': (generic_lock, [['-d']]),
                       'lock_without_sleep': (generic_lock, []),
                       'inactive_lock': (watchdog_lock, [5]),
                       'watchdog_lock': (watchdog_lock_wrapper, []),
                       'short_inactive_lock': (watchdog_lock, [3, 30]),
                       'suspend_or_lock': (watchdog_lock, [1, 15]),
                       'blur': (generic_blur, []),
                       'blur_with_sleep': (generic_blur, [['-d']]),
                       'freeze': (freeze, []),
                       'logout': (subprocess.call, [['i3-msg', 'exit']]),
                       'suspend': (suspend, [True]),
                       'hibernate': (hibernate, []),
                       'reboot': (subprocess.call, [['systemctl', 'reboot']]),
                       'shutdown': (subprocess.call,
                                    [['systemctl', 'poweroff']]),
                       'usage': (usage, []),
                       'black': (plain_lock, [['-c', '000000']]),
                       'white': (plain_lock, [['-c', 'ffffff']]),
                       }

        func, args = option_dict[arguments["input"]]
        func(*args)
        # _log()
    except (IndexError, KeyError):
        usage()
        # _log()
        exit(1)


if __name__ == '__main__':
    _log()
    main()
