#!/usr/bin/python3

import sys

try:
    print({
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
    }[sys.argv[1].lower()])
except IndexError:
    print('.')
except KeyError:
    print('WARNING: INVALID INPUT', file=sys.stderr)
    print('.')
