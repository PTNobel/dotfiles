#!/usr/bin/python3

import time
import sys
import fcntl
import subprocess


def modify_lock(operation: int) -> bool:
    try:
        fd = open("/tmp/.recentworkspace.lock")
    except FileNotFoundError:
        fd = open("/tmp/.recentworkspace.lock", 'a')

    try:
        fcntl.flock(fd, operation)
        return False
    except OSError:
        return True


def block_run() -> bool:
    return modify_lock(fcntl.LOCK_EX | fcntl.LOCK_NB)


def unblock_run() -> bool:
    return modify_lock(fcntl.LOCK_UN | fcntl.LOCK_NB)


def main() -> None:
    if len(sys.argv) != 2:
        exit(2)
    
    if block_run():
        exit(3)
    elif sys.argv[1] == "prev":
        subprocess.call(["i3-msg", "workspace", "prev_on_output"])
    elif sys.argv[1] == "next":
        subprocess.call(["i3-msg", "workspace", "next_on_output"])

    time.sleep(0.5)
    unblock_run()


if __name__ == '__main__':
    main()
