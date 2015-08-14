#!/usr/bin/python3

import os
import process


def prompt_user(secret_num=0):
    if secret_num >= 5:
        exit(1)
    else:
        try:
            user_input = input('Do you want to launch mpd? ([Y]es|[N]o) '
                               ).lower()
        except EOFError:
            exit(0)
        if len(user_input) == 0:
            prompt_user(secret_num + 1)
        if user_input[0] == 'y':
            os.system('mpd.sh ; ncmpcpp')
        elif user_input[0] == 'n':
            exit(0)
        else:
            prompt_user(secret_num + 1)


if process.is_comm_running('mpd'):
    os.system('ncmpcpp')

else:
    prompt_user()
