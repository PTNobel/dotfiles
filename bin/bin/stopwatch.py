#!/usr/bin/env python3

import sys
import time


def makeTimeString(cur_time, maxNumber):
    _minutes_str = str()
    _hour_str = str()
    _hour = (cur_time >= 60**2 or maxNumber >= 60**2)
    _minutes = (cur_time >= 60 or maxNumber >= 60)

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


def turnNumToNiceString(cur_time, maxTime):
    math_time = maxTime - cur_time
    final_str = str()
    _minute_str = str()
    _hour_str = str()
    _day_str = str()
    _second_str = str()
    _hour = (math_time >= 60**2)
    _minute = (math_time >= 60)
    _day = (math_time >= 60**2 * 24)
    _second = (math_time % 60 == 0)
    if _day:
        _day_str = str(math_time % (60**2 * 24))
        _day_str += 'd'
    if _hour:
        _hour_str = str(math_time % (60**2))
        _hour_str += 'h'
        pass
    if _minute:
        _minute_str = str(math_time % (60))
        _minute_str += 'm'
    if _second:
        _second_str = str(math_time % 60)
        _second_str += 's'

    for i in [_day_str, _hour_str, _minute_str, _second_str]:
        if i:
            final_str += i
            final_str += ' '
    return final_str

if len(sys.argv) == 1:
    exit(1)

cur_number = int()
for j in sys.argv[1:]:
    cur_number += int(j[:-1])
    if j[-1] == 'm':
        cur_number *= 60
    elif j[-1] == 'h':
        cur_number *= 60**2
    elif j[-1] == 'd':
        cur_number *= 60**2 * 24
    print(cur_number)
'''
if sys.argv[1][:-1].isdigit():
    number = int(sys.argv[1][:-1])

if sys.argv[1][-1] == 's' or sys.argv[1][-1].isdigit():
    pass
elif sys.argv[1][-1] == 'm':
    number *= 60
elif sys.argv[1][-1] == 'h':
    number *= 60**2
elif sys.argv[1][-1] == 'd':
    number *= 60**2 * 24
'''
number = cur_number
endTime = makeTimeString(number, number)
try:
    for i in range(number):
        print('\r' + makeTimeString(i, number) + '/' + endTime, end='')
        time.sleep(1)
except KeyboardInterrupt:
    print('\n' + turnNumToNiceString(i, number))
    exit(4)
