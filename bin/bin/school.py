#!/usr/bin/python3

import sys

try:
    print({
        "hug": "HUG",
        "el": "EL",
        "ush": "USH",
        "chem": "Chem",
        "calc": "Calc",
        "photo": "Photo",
    }[sys.argv[1].lower()])
except IndexError:
    print('.')
