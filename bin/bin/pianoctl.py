#!/usr/bin/python

import os

if os.system('pidof pianobar') == 0:
    os.system('pianoctl')

else:
    user_input = input('Do you want to launch pianctl?').lower()
    if user_input == 'y' or user_input == "yes":
        os.system('pianoctl')
    elif user_input == 'n' or user_input == "no":
        exit(1)