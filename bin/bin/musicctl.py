#!/usr/bin/python3

# A python3 port of musicctl.sh.

import time
import os
import sys


def warning(*objs, prefix='WARNING: '):
    printed_list = str(prefix)
    for i in objs:
        printed_list += i
    print(printed_list, file=sys.stderr)


def usage(exit_code, name_of_program='musicctl.py'):
    verboseprint('usage() starting', exit_code, name_of_program)
    usage_text = "Usage: " + name_of_program + \
        " {[a command]|player|commands|usage|help}"
    if exit_code == 0:
        print(usage_text)
    elif exit_code > 0:
        warning(usage_text, prefix='')
    else:
        exit_code = abs(exit_code)
    exit(exit_code)


if os.getenv('VERBOSE') == '1':
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to stuff
        # everything to be printed into a string.
        for arg in args:
            print(arg)


else:
    def verboseprint(*args):
        return

verboseprint("Defining verboseprint")


def processargs(input_argv):
    verboseprint('start proccessargs')

    def help(input_dict):
        usage(0, input_dict["name"])
        return input_dict

    def verbose(input_dict):
        input_dict["verbose"] = True
        input_dict["test_mode_suffix"] = ''
        return input_dict

    def trial(input_dict):
        input_dict["test_mode_prefix"] = 'echo '
        input_dict["test_mode_suffix"] = ''
        return input_dict

    long_args_to_disc = {'--help': help, '--verbose': verbose,
                         '--trial': trial}
    short_args_to_disc = {'h': help, 'v': verbose,
                          't': trial}
    output = {"verbose": None, "input": None, 'test_mode_prefix': '',
              'test_mode_suffix': ' >/dev/null', 'argv': input_argv,
              "name": os.path.basename(input_argv[0]),
              }
    if len(input_argv) == 1:
        warning("Not enough arguments")
        usage(1, output["name"])
    else:
        for i in range(1, len(input_argv)):
            verboseprint("Index:", i, input_argv, output)
            if len(input_argv[i]) >= 2 and input_argv[i][0:2] == '--':
                try:
                    verboseprint(long_args_to_disc[input_argv[i]])
                    output = long_args_to_disc[input_argv[i]](output)
                    verboseprint(output)
                except KeyError:
                    warning("Invalid argument", prefix='')
                    usage(1, output["name"])

            elif input_argv[i][0] == '-' and input_argv[i][1] != '-':
                for j in range(1, len(input_argv[i])):
                    try:
                        verboseprint(short_args_to_disc[input_argv[i][j]])
                        output = short_args_to_disc[input_argv[i][j]](output)
                        verboseprint(output)
                    except KeyError:
                        warning("Invalid argument", prefix='')
                        usage(1, output["name"])

            elif output["input"] is None:
                output["input"] = input_argv[i]

            else:
                warning("Error parsing arguments")
                verboseprint(
                    output,
                    input_argv,
                    i,
                    input_argv[i],
                    output["input"])
                usage(1, output["name"])

    verboseprint('returning', output)
    verboseprint('end processargs')
    return output


processed_args = processargs(sys.argv)

if processed_args["verbose"]:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to stuff
        # everything to be printed into a string.
        for arg in args:
            print(arg)
    verboseprint("Defining verboseprint")


else:
    def verboseprint(*args):
        return


def get_keys(command_dict):
    for i in sorted(command_dict.keys()):
        print("For player " + i + " the following commands are available:")
        for j in sorted(command_dict[i].keys()):
            print("   " + j)
    usage(-256, '')


class mpd:

    def __init__(self, processed_args):
        verboseprint('mpd is being inited')
        self.system_prefix = processed_args['test_mode_prefix']
        self.system_suffix = processed_args['test_mode_suffix']
        self.commands = {'mpd': {'play': self.pause, 'pause': self.pause,
                                 'back': self.back, 'next': self.next,
                                 'quit': self.stop, 'stop': self.stop}}

    def pause(self):
        verboseprint('mpd.pause has been called')
        os.system(self.system_prefix + 'mpc toggle' + self.system_suffix)

    def back(self):
        verboseprint('mpd.back has been called')
        os.system(self.system_prefix + 'mpc prev' + self.system_suffix)

    def next(self):
        verboseprint('mpd.next has been called')
        os.system(self.system_prefix + 'mpc next' + self.system_suffix)

    def stop(self):
        verboseprint('mpd.stop has been called')
        os.system(self.system_prefix + 'mpc stop' + self.system_suffix)


class pianobar:

    def __init__(self, processed_args):
        verboseprint('pianobar is being inited')
        self.system_prefix = processed_args['test_mode_prefix']
        self.system_suffix = processed_args['test_mode_suffix']
        self.commands = {'pianobar': {'play': self.pause, 'pause': self.pause,
                                      'back': self.like, 'next': self.next,
                                      'quit': self.stop, 'stop': self.stop,
                                      'tired': self.tired, 'like': self.like}}

    def pause(self):
        verboseprint('pianobar.pause has been called')
        os.system(self.system_prefix + 'pianoctl p' + self.system_suffix)

    def like(self):
        verboseprint('pianobar.back has been called')
        os.system(self.system_prefix + 'pianoctl +' + self.system_suffix)

    def next(self):
        verboseprint('pianobar.next has been called')
        os.system(self.system_prefix + 'pianoctl n' + self.system_suffix)

    def stop(self):
        verboseprint('pianobar.stop has been called')
        os.system(self.system_prefix + 'pianoctl q' + self.system_suffix)
        time.sleep(1)
        if os.system("pidof pianobar") == 0:
            os.system("killall pianobar")

    def tired(self):
        verboseprint('pianobar.tired has been called')
        os.system(self.system_prefix + 'pianoctl t' + self.system_suffix)


class playerctl:

    def __init__(self, processed_args):
        verboseprint('playerctl is being inited')
        self.system_prefix = processed_args['test_mode_prefix']
        self.system_suffix = processed_args['test_mode_suffix']
        self.commands = {'playerctl': {'play': self.pause, 'pause': self.pause,
                                       'back': self.back, 'next': self.next,
                                       'quit': self.stop, 'stop': self.stop}}

    def pause(self):
        verboseprint('playerctl.pause has been called')
        os.system(self.system_prefix + 'playerctl play-pause' +
                  self.system_suffix)

    def back(self):
        verboseprint('playerctl.back has been called')
        os.system(self.system_prefix + 'playerctl previous' +
                  self.system_suffix)

    def next(self):
        verboseprint('playerctl.next has been called')
        os.system(self.system_prefix + 'playerctl next' + self.system_suffix)

    def stop(self):
        verboseprint('playerctl.stop has been called')
        os.system(self.system_prefix + 'playerctl stop' + self.system_suffix)


def which_player():
    output = str()
    processes = [
        open(os.path.join('/proc', pid, 'comm'), 'r').read().strip('\n')
        for pid in os.listdir('/proc') if pid.isdigit()]

    verboseprint(processes)

    if 'mpd' in processes:
        # pianobar get priority over mpd, unless mpd is playing.
        if 'pianobar' in processes:
            if os.system("mpc status | grep playing &>/dev/null") == 0:
                output = "mpd"
            else:
                output = "pianobar"
        else:
            output = "mpd"
    elif 'pianobar' in processes:
        output = "pianobar"
    else:
        output = 'playerctl'
    return output


def main(arguments):
    verboseprint('main() starting')
    verboseprint(arguments)
    # Handle help and usage correctly:
    if arguments["input"] == "usage" or arguments["input"] == "help":
        usage(0, arguments["name"])

    # Figure out what player is running.
    player = which_player()
    if arguments["input"] == "player":
        print(player)
        usage(-256, arguments['name'])

    # Create a two dimensional dictionary. first key specifies player and the
    # second one is the specific command. It'll be the function to call. It's
    # possible to define commands that are specific to a player.
    commands = dict()
    for i in [pianobar(arguments), mpd(arguments), playerctl(arguments)]:
        commands.update(i.commands)

    verboseprint(commands)
    if arguments["input"] == "commands":
        get_keys(commands)

    # Catching a KeyError should prevent this from exploding over the user
    # giving invalid input, though it also prevents bad players from being
    # spotted. So make sure all new players are followed by thorough testing,
    # or just make sure you use the same spelling everywhere.
    try:
        verboseprint(commands[player][arguments["input"]])
        commands[player][arguments["input"]]()
    except KeyError:
        warning("Invalid input.")
        usage(1, arguments["name"])


if __name__ == "__main__":
    main(processed_args)
