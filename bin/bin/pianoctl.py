#!/usr/bin/python3

import os

def prompt_user(secret_num=0):
    if secret_num >= 5:
        exit(1)
    else:
        try:
            user_input = input('Do you want to launch pianoctl? ([Y]es|[N]o) ').lower()
        except EOFError:
            exit(0)
        if user_input == 'y' or user_input == "yes":
            os.system('pianoctl')
        elif user_input == 'n' or user_input == "no" or user_input == "\n":
            exit(1)
        else:
            prompt_user(secret_num+1)

if os.system('pidof pianobar >/dev/null') == 0:
    os.system('pianoctl')

else:
    prompt_user()
