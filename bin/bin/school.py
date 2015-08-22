#!/usr/bin/python3

import sys

try:
    print({
        "hug": "HUG",
        "el": "EL",
        "ush": "USH",
        "chem": "Chem",
        "alchemy": "Alchemy",
        "calc": "Calc",
        "photo": "Photo",
    }[sys.argv[1].lower()])
except IndexError:
    print('.')
except KeyError:
    print('WARNING: INVALID INPUT', file=sys.stderr)
    print('.')
