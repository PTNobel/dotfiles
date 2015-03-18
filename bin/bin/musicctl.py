#!/usr/bin/python3

# A python3 port of the bash musicctl program. Should be a drop in replacment.

import os
import sys


def warning(*objs, prefix='WARNING: '):
    printed_list = str(prefix)
    for i in objs:
        printed_list += i
    print(printed_list, file=sys.stderr)


def usage(exit_code, name_of_program):
    usage_text = "Usage: " + name_of_program + \
        " {play|pause|back|stop|next|toggle|usage|help}"
    if exit_code == 0:
        print(usage_text)
    elif exit_code > 0:
        warning(usage_text, prefix='')
    else:
        exit_code = 1
    exit(exit_code)


def processargs(argv, verbose_check=False):
    if verbose_check:
        if '-v' in argv or '--verbose' in argv:
            output = True
        else:
            output = False
    else:
        output = {"verbose": None, "input": None}
        output["name"] = argv[0]
        if len(argv) == 1:
            warning("Not enough arguments")
            usage(1, output["name"])
        elif len(argv) >= 2:
            if argv[-1] == "help" or argv[-1] == "usage":
                usage(0, output["name"])

            else:
                output["input"] = argv[-1]
        for i in argv:
            if i == "-h":
                usage(0, output["name"])
            if i == "-v" or i == "--verbose":
                output["verbose"] = True
    return output


if processargs(sys.argv, verbose_check=True):
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to
        # stuff everything to be printed into a single string
        for arg in args:
            print(arg)
else:
    def verboseprint(*args):
        return


def main(raw_argv):
    arguments = processargs(raw_argv)
    # TODO replace get_player()
    if os.system("pidof mpd >/dev/null") == 0:
        if os.system("pidof pianobar >/dev/null") == 0:
            if os.system("mpc status | grep playing &>/dev/null") == 0:
                player = "mpd"
            else:
                player = "pianobar"
        else:
            player = "mpd"
    elif os.system("pidof pianobar >/dev/null") == 0:
        player = "pianobar"
    else:
        warning("No music player found")
        usage(-1)

    program_name = arguments["name"]
    operation = arguments["input"]
    verboseprint(player)
    pianobar_dict = {'play': "pianoctl p", 'pause': "pianoctl p",
                     'back': "pianoctl +", 'next': "pianoctl -",
                     'quit': "pianoctl q", 'stop': "pianoctl q ; " +
                     "sleep 3 ; pidof pianobar && killall pianobar",
                     'tired': "pianoctl t"}
    mpd_dict = {'play': "mpc toggle", 'pause': "mpc toggle",
                'back': "mpc prev", 'next': "mpc next",
                'quit': "mpc stop", 'stop': "mpc stop"}
    commands = {'pianobar': pianobar_dict, 'mpd': mpd_dict}
    verboseprint(commands)
    try:
        verboseprint(commands[player][operation])
        os.system(commands[player][operation])
    except KeyError:
        warning("Invalid input")
        usage(1, program_name)


if __name__ == "__main__":
    main(sys.argv)
