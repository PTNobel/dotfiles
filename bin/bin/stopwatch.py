#!/usr/bin/env python3

import sys
import time


def makeTimeString(cur_time, maxNumber):
    _minutes = False
    _hour = False
    _minutes_str = str()
    _hour_str = str()
    if maxNumber >= 60**2:
        _hour = True
        _minutes = True
    elif maxNumber >= 60:
        _minutes = True

    if _minutes:
        _minutes_str = str((cur_time // 60) % 60**2) + ':'
        if len(_minutes_str) <= 2:
            _minutes_str = '0' + _minutes_str

    if _hour:
        _hour_str = str(cur_time // 60**2) + ':'
        if len(_hour_str) <= 2:
            _hour_str = '0' + _hour_str

    _second_str = str(cur_time % 60)
    if len(_second_str) <= 1:
        _second_str = '0' + _second_str
    return _hour_str + _minutes_str + _second_str


if len(sys.argv) == 1:
    exit(1)
elif sys.argv[1][:-1].isdigit():
    number = int(sys.argv[1][:-1])

if sys.argv[1][-1] == 's' or sys.argv[1][-1].isdigit():
    pass
elif sys.argv[1][-1] == 'm':
    number *= 60
elif sys.argv[1][-1] == 'h':
    number *= 60**2
elif sys.argv[1][-1] == 'd':
    number *= 60**2 * 24

endTime = makeTimeString(number, number)
for i in range(number):
    print('\r' + makeTimeString(i, number) + '/' + endTime, end='')
    time.sleep(1)
