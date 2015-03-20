#!/usr/bin/python3

# A python3 port of musicctl.sh.

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
        exit_code = abs(exit_code)
    exit(exit_code)


def old_processargs(argv, verbose_check=False):
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


def processargs(argv, verbose_check=False):
    if verbose_check:
        if '-v' in argv or '--verbose' in argv:
            output = True
        else:
            output = False
    else:
        indexes_to_ignore = list()
        supported_arguments = ['-h', '--help', '-v', '--verbose']
        output = {"verbose": None, "input": None}
        output["name"] = argv[0]

        if len(argv) == 1:
            warning("Not enough arguments")
            usage(1, output["name"])

        else:
            for i in range(1, len(argv)):
                if i in indexes_to_ignore:
                    continue
                else:
                    if argv[i][0] == '-':
                        verboseprint("Argument found :"+argv[i]+" Index is "+i)
                        if argv[i] not in supported_arguments:
                            warning("Invalid argument", prefix='')
                            usage(1, output["name"])

                        else:
                            if argv[i] == '-h' or argv[i] == '--help':
                                usage(0, output["name"])
                            elif argv[i] == "-v" or argv[i] == "--verbose":
                                output["verbose"] = True

                    else:
                        output["input"] = argv[i]
    return output


if processargs(sys.argv, verbose_check=True):
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to stuff
        # everything to be printed into a string.
        for arg in args:
            print(arg)
else:
    def verboseprint(*args):
        return


def main(raw_argv):
    # Arguments is being defined here to insure it's available for the first
    # usage call.
    arguments = processargs(raw_argv)
    verboseprint(arguments)
    # Handle help and usage correctly:
    if arguments["input"] == "usage" or arguments["input"] == "help":
        usage(0, arguments["name"])

    # Figure out what player is running.
    if os.system("pidof mpd >/dev/null") == 0:
        # pianobar get priority over mpd, unless mpd is playing.
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
        # - vaue for usage, because there's no need to print how to use the
        # program when there's no player.
        warning("No music player found")
        usage(-1, arguments["name"])
    verboseprint(player)

    # Create a two dimensional dictionary. first key specifies player and the
    # second one is the specific command. It'll be the command to pass to
    # os.system(). It's possible to define commands that are specific to a
    # player.
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

    # Catching a KeyError should prevent this from exploding over the user
    # giving invalid input
    try:
        verboseprint(commands[player][arguments["input"]])
        os.system(commands[player][arguments["input"]] + ' >/dev/null')
    except KeyError:
        warning("Invalid input")
        usage(1, arguments["name"])


if __name__ == "__main__":
    main(sys.argv)
