#!/usr/bin/python3

import subprocess
import process


def prompt_user(secret_num=0):
    if secret_num >= 5:
        exit(1)
    else:
        try:
            user_input = input('Do you want to launch mpd, pianobar,' +
                               ' or neither? ([m]|[p]]|[n]) '
                               ).lower()
        except EOFError:
            exit(0)
        if len(user_input) == 0:
            prompt_user(secret_num + 1)
        elif user_input[0] == 'm':
            subprocess.call(['mpd.sh'])
            subprocess.call(['ncmpcpp'])
        elif user_input[0] == 'p':
            subprocess.call(['pianoctl'])
        elif user_input[0] == 'n':
            exit(0)
        else:
            prompt_user(secret_num + 1)


def main():
    while True:
        process.update_buffers()
        if process.is_comm_running('pianobar'):
            subprocess.call(['pianoctl'])

        elif process.is_comm_running('mpd'):
            subprocess.call(['ncmpcpp'])

        else:
            prompt_user()

if __name__ == '__main__':
    main()
