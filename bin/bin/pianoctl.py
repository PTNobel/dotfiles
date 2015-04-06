#!/usr/bin/python3

from os import system


def prompt_user(secret_num=0):
    if secret_num >= 5:
        exit(1)
    else:
        try:
            user_input = input('Do you want to launch pianobar? ([Y]es|[N]o) '
                               ).lower()
        except EOFError:
            exit(0)
        if len(user_input) == 0:
            prompt_user(secret_num+1)
        if user_input[0] == 'y':
            system('pianoctl')
        elif user_input[0] == 'n':
            exit(0)
        else:
            prompt_user(secret_num + 1)


if system('pidof pianobar >/dev/null') == 0:
    system('pianoctl')

else:
    prompt_user()
