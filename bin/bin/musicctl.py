#!/usr/bin/python3

# A python3 port of musicctl.sh.

import time
import os
import sys
import re


# warning() functions like print, except it prefixes everything and prints to
# stderr.
def warning(*objs, prefix='WARNING: '):
    printed_list = str(prefix)
    for i in objs:
        printed_list += str(i)
    print(printed_list, file=sys.stderr)


def usage(exit_code, name):
    verboseprint('usage() starting', exit_code, name)
    usage_text = "Usage: " + name + \
        " {[a command]|player|commands|usage|help}"

    if exit_code == 0:
        print(usage_text)
    elif exit_code > 0:
        warning(usage_text, prefix='')
    elif exit_code < 0:
        verboseprint('Wait a negative exit_code to usage(), what?')
        usage(exit_code, name)
    exit(exit_code)


# setting VERBOSE to 1 in environ, will turn verbose mode on, during
# processargs().
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

    # All of these run in the same scope as processargs(). They make changes to
    # output.
    def help():
        usage(0, output['name'])

    def verbose():
        output["verbose"] = True
        output["test_mode_suffix"] = ''

    def trial():
        output["test_mode_prefix"] = 'echo '
        output["test_mode_suffix"] = ''

    def player():
        if '=' in input_argv[i]:
            output["player"] = input_argv[i].split('=')[1]
        else:
            output["player"] = input_argv[i + 1]
            indexes_to_ignore.append(i + 1)

    # In place of a switch-case statement the following dictionaires link argv
    # entries to functions.
    long_args_to_disc = {'--help': help, '--verbose': verbose,
                         '--trial': trial, '--player': player}
    short_args_to_disc = {'h': help, 'v': verbose, 't': trial, 'p': player}
    output = {"verbose": None,
              "input": None,
              "test_mode_prefix": '',
              "test_mode_suffix": ' >/dev/null',
              "name": os.path.basename(input_argv[0]),
              "player": None,
              }
    indexes_to_ignore = list()

    if len(input_argv) == 1:
        warning("Not enough arguments")
        usage(1, output['name'])
    else:
        # range() starts at 1 to prevent the name from being processed.
        for i in range(1, len(input_argv)):
            verboseprint("Index:", i, input_argv, output)
            if i in indexes_to_ignore:
                continue

            elif len(input_argv[i]) >= 2 and input_argv[i][0:2] == '--':
                try:
                    long_args_to_disc[input_argv[i].split('=')[0]]()
                    verboseprint(output)
                except KeyError:
                    verboseprint(long_args_to_disc[
                        input_argv[i].split('=')[0]])
                    verboseprint(input_argv[i].split('=')[0])
                    warning("Invalid argument", prefix='')
                    usage(1, output['name'])

            elif input_argv[i][0] == '-' and input_argv[i][1] != '-':
                for j in range(1, len(input_argv[i])):
                    try:
                        short_args_to_disc[input_argv[i][j]]()
                        verboseprint(output)
                    except KeyError:
                        verboseprint(short_args_to_disc[input_argv[i][j]])
                        warning("Invalid argument", prefix='')
                        usage(1, output['name'])

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
                usage(1, output['name'])

    verboseprint('returning', output)
    verboseprint('end processargs')
    return output

# global arguments
arguments = processargs(sys.argv)


if arguments["verbose"]:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to stuff
        # everything to be printed into a string.
        for arg in args:
            print(arg)
    verboseprint("Defining verboseprint")

else:
    def verboseprint(*args):
        return


def get_keys(list_of_classes):
    for i in list_of_classes:
        print("For player " + str(i) +
              " the following commands are available:")
        for j in sorted(i.commands.keys()):
            print("   " + j)

    exit(0)


''' # An example implementation of a player class
class generic:

    def __init__(self):
        verboseprint('generic is being inited')
        self.system_prefix = arguments['test_mode_prefix']
        self.system_suffix = arguments['test_mode_suffix']
        self.name = 'generic'
        self.commands = {'play': self.pause, 'pause': self.pause,
                         'back': self.back, 'next': self.next,
                         'quit': self.stop, 'stop': self.stop,
                         }

    def pause(self):
        verboseprint('generic.pause has been called')
        os.system(self.system_prefix + '' + self.system_suffix)

    def back(self):
        verboseprint('generic.back has been called')
        os.system(self.system_prefix + '' + self.system_suffix)

    def next(self):
        verboseprint('generic.next has been called')
        os.system(self.system_prefix + '' + self.system_suffix)

    def stop(self):
        verboseprint('generic.stop has been called')
        os.system(self.system_prefix + '' + self.system_suffix)


'''


class mpd:

    def __init__(self):
        verboseprint('mpd is being inited')
        self.system_prefix = arguments['test_mode_prefix']
        self.system_suffix = arguments['test_mode_suffix']
        self.name = 'mpd'
        self.commands = {'play': self.pause, 'pause': self.pause,
                         'back': self.back, 'next': self.next,
                         'quit': self.stop, 'stop': self.stop,
                         'is_playing': self.is_playing}

    def __repr__(self):
        return self.name

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

    def is_playing(self):
        exit_code = os.system('mpc status | grep playing' + self.system_suffix)
        verboseprint(exit_code)

        if exit_code == 0:
            exit(0)
        else:
            exit(1)


class pianobar:

    def __init__(self):
        verboseprint('pianobar is being inited')
        self.system_prefix = arguments['test_mode_prefix']
        self.system_suffix = arguments['test_mode_suffix']
        self.name = 'pianobar'
        self.commands = {'play': self.pause, 'pause': self.pause,
                         'back': self.like, 'next': self.next,
                         'quit': self.stop, 'stop': self.stop,
                         'tired': self.tired, 'like': self.like,
                         'dislike': self.dislike,
                         'is_playing': self.is_playing}

    def __repr__(self):
        return self.name

    def pause(self):
        verboseprint('pianobar.pause has been called')
        os.system(self.system_prefix + 'pianoctl p' + self.system_suffix)

    def like(self):
        verboseprint('pianobar.back has been called')
        os.system(self.system_prefix + 'pianoctl +' + self.system_suffix)

    def dislike(self):
        verboseprint('pianobar.back has been called')
        os.system(self.system_prefix + 'pianoctl -' + self.system_suffix)

    def next(self):
        verboseprint('pianobar.next has been called')
        os.system(self.system_prefix + 'pianoctl n' + self.system_suffix)

    def stop(self):
        verboseprint('pianobar.stop has been called')
        os.system(self.system_prefix + 'pianoctl q' + self.system_suffix)
        # if pianobar isn't responding kill it.
        time.sleep(1)
        if os.system("pidof pianobar") == 0:
            os.system("killall pianobar")

    def tired(self):
        verboseprint('pianobar.tired has been called')
        os.system(self.system_prefix + 'pianoctl t' + self.system_suffix)

    def is_playing(self):
        log1_time_stamp = self._get_time()
        time.sleep(2)
        log2_time_stamp = self._get_time()
        verboseprint(log1_time_stamp, log2_time_stamp,
                     log1_time_stamp == log2_time_stamp)

        if log1_time_stamp == log2_time_stamp:
            exit(1)
        else:
            exit(0)

    def _get_time(self):
        """Reads the pianobar time, and returns a str() of syntax '##:##/##:##'
        if it can't do that it'll exit(1)"""
        log = open(os.path.expanduser('~/.config/pianobar/out'), 'r')
        time_stamp = log.read()[-12:-1]
        log.close()
        if re.match(r'^\d{2}:\d{2}/\d{2}:\d{2}$', time_stamp):
            return time_stamp
        else:
            verboseprint('FAILED REGEX:', time_stamp)
            exit(1)


class playerctl:

    def __init__(self):
        verboseprint('playerctl is being inited')
        self.system_prefix = arguments['test_mode_prefix']
        self.system_suffix = arguments['test_mode_suffix']
        self.name = 'playerctl'
        self.commands = {'play': self.pause, 'pause': self.pause,
                         'back': self.back, 'next': self.next,
                         'quit': self.stop, 'stop': self.stop,
                         'is_playing': self.is_playing}

    def __repr__(self):
        return self.name

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

    def is_playing(self):
        exit_code = os.system('playerctl status | grep Playing' +
                              self.system_suffix)
        verboseprint(exit_code)

        if exit_code == 0:
            exit(0)
        else:
            exit(1)


def which_player(arguments):
    def get_comm_of_pid(pid):
        try:
            comm_file = open(os.path.join('/proc', pid, 'comm'), 'r')
            comm = comm_file.read().rstrip('\n')
            comm_file.close()
        except FileNotFoundError:
            comm = None
        return comm

    def list_pids():
        return [pid for pid in os.listdir('/proc') if pid.isdigit()]

    output = str()
    if arguments['player'] is not None:
        output = {
            'mpd': mpd,
            'pianobar': pianobar,
            'playerctl': playerctl}[
            arguments['player']]
    else:
        processes = [comm for comm in
                     map(get_comm_of_pid, list_pids()) if comm is not None]

        verboseprint(processes)

        # pianobar get priority over mpd, unless mpd is playing.
        if 'mpd' in processes:
            if 'pianobar' in processes:
                if os.system("mpc status | grep playing &>/dev/null") == 0:
                    output = mpd
                else:
                    output = pianobar
            else:
                output = mpd
        elif 'pianobar' in processes:
            output = pianobar
        else:
            output = playerctl

    return output()


def main(arguments):
    verboseprint('main() starting')
    verboseprint(arguments)
    # Handle help and usage correctly:
    if arguments["input"] == "usage" or arguments["input"] == "help":
        usage(0, arguments['name'])

    if arguments["input"] == "commands":
        get_keys([pianobar(), mpd(), playerctl()])

    # Figure out what player is running.
    player = which_player(arguments)
    if arguments["input"] == "player":
        print(player)
        exit(0)

    # Catching a KeyError should prevent this from exploding over the user
    # giving invalid input.
    try:
        verboseprint(player)
        verboseprint(player.commands[arguments["input"]])
        player.commands[arguments["input"]]()
    except KeyError:
        warning("Invalid input.")
        usage(1, arguments['name'])


if __name__ == "__main__":
    main(arguments)
