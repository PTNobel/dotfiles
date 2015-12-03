#!/usr/bin/python3

import sys

try:
    if sys.argv[1] == 'b' and len(sys.argv) > 2:
        path = 'bitbucket/'
        num = 2
    else:
        path = ''
        num = 1
    path += {
        "hug": "HUG",
        "h": "HUG",
        "el": "EL",
        "e": "EL",
        "ush": "USH",
        "u": "USH",
        "alchemy": "Alchemy",
        "a": "Alchemy",
        "calc": "Calc",
        "c": "Calc",
        "photo": "Photo",
        "p": "Photo",
        "speech": "Speech_and_Debate",
        "debate": "Speech_and_Debate",
        "s": "Speech_and_Debate",
        "m": "MUN",
        "b": "bitbucket",
    }[sys.argv[num].lower()]
    print(path)
except IndexError:
    print('.')
except KeyError:
    print('WARNING: INVALID INPUT', file=sys.stderr)
    print('.')
