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


def processargs(argv):
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

arguments = processargs(sys.argv)

if arguments["verbose"]:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to
        # stuff everything to be printed into a single string
        for arg in args:
            print(arg)
else:
    def verboseprint(*args):
        return


class musicctl:

    def __init__(self, program_arguments):
        self.get_player()
        self.program_name = program_arguments["name"]
        self.operation = program_arguments["input"]
        verboseprint(self.player)
        self.make_command_dict()
        self.communicate_with_player()

    def make_command_dict(self):
        self.pianobar_dict = {'play': "pianoctl p", 'pause': "pianoctl p",
                              'back': "pianoctl +", 'next': "pianoctl -",
                              'quit': "pianoctl q", 'stop': "pianoctl q ; \
                              sleep 3 ; pidof pianobar && killall pianobar",
                              'tired': "pianoctl t"}
        self.mpd_dict = {'play': "mpc toggle", 'pause': "mpc toggle",
                         'back': "mpc prev", 'next': "mpc next",
                         'quit': "mpc stop", 'stop': "mpc stop"}
        self.commands = {'pianobar': self.pianobar_dict, 'mpd': self.mpd_dict}

    def get_player(self):
        if os.system("pidof mpd >/dev/null") == 0:
            if os.system("pidof pianobar >/dev/null") == 0:
                if os.system("mpc status | grep playing &>/dev/null") == 0:
                    self.player = "mpd"
                else:
                    self.player = "pianobar"
            else:
                self.player = "mpd"
        elif os.system("pidof pianobar >/dev/null") == 0:
            self.player = "pianobar"
        else:
            warning("No music player found")
            usage(-1)

    def communicate_with_player(self):
        try:
            verboseprint('In communicate_with_player')
            verboseprint(self.commands[self.player][self.operation])
            os.system(self.commands[self.player][self.operation])
        except KeyError:
            warning("Invalid input")
            usage(1, self.program_name)

music = musicctl(arguments)
