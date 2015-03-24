#!/usr/bin/python3

import os


def prompt_user(secret_num=0):
    if secret_num >= 5:
        exit(1)
    else:
        try:
            user_input = input('Do you want to launch pianoctl? ([Y]es|[N]o) '
                               ).lower()
        except EOFError:
            exit(0)
        if user_input[0] == 'y':
            os.system('pianoctl')
        elif user_input[0] == 'n':
            exit(0)
        else:
            prompt_user(secret_num+1)

if os.system('pidof pianobar >/dev/null') == 0:
    os.system('pianoctl')

elif True:
    prompt_user()

elif 'ctl' in os.listdir(os.environ['HOME'] + '/.config/pianobar/'):
    None

else:
    prompt_user()
