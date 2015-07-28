#!/usr/bin/python3

# A python3 port of musicctl.sh.

import time
import os
import sys
import re
import process


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


# setting VERBOSE to 1 in environ, will turn verbose mode on for processargs().
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
    def _help():
        usage(0, output['name'])

    def _verbose():
        output["verbose"] = True
        output["test_mode_suffix"] = ''

    def _trial():
        output["test_mode_prefix"] = 'echo '
        output["test_mode_suffix"] = ''

    def _player():
        if '=' in input_argv[i]:
            output["player"] = input_argv[i].split('=')[1]
        else:
            output["player"] = input_argv[i + 1]
            indexes_to_ignore.append(i + 1)

    # In place of a switch-case statement the following dictionaires link argv
    # entries to functions.
    long_args_to_disc = {'--help': _help, '--verbose': _verbose,
                         '--trial': _trial, '--player': _player}
    short_args_to_disc = {'h': _help, 'v': _verbose, 't': _trial, 'p': _player}
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
    name = 'generic'
    system_prefix = arguments['test_mode_prefix']
    system_suffix = arguments['test_mode_suffix']

    def __init__(self):
        verboseprint('generic is being inited')
        self.commands = {'play': self.pause, 'pause': self.pause,
                         'back': self.back, 'next': self.next,
                         'quit': self.stop, 'stop': self.stop,
                         }

    def __repr__(self):
        return self.name

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
    name = 'mpd'
    system_prefix = arguments['test_mode_prefix']
    system_suffix = arguments['test_mode_suffix']

    def __init__(self):
        verboseprint('mpd is being inited')
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
    name = 'pianobar'
    system_prefix = arguments['test_mode_prefix']
    system_suffix = arguments['test_mode_suffix']

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
        process.update_buffers()
        if process.is_comm_running("pianobar"):
            os.system("killall pianobar")

    def tired(self):
        verboseprint('pianobar.tired has been called')
        os.system(self.system_prefix + 'pianoctl t' + self.system_suffix)

    def is_playing(self):
        log1_time_stamp, success1 = self._get_time()
        verboseprint(log1_time_stamp)
        time.sleep(2)
        log2_time_stamp, success2 = self._get_time()
        verboseprint(log2_time_stamp,
                     log1_time_stamp == log2_time_stamp)

        if not (success1 and success2):
            exit(1)
        if log1_time_stamp == log2_time_stamp:
            exit(1)
        else:
            exit(0)

    def _get_time(self, tries=0):
        """Reads the pianobar time, and returns a tuple of  str '##:##/##:##'
        and a boolean which reflects whether it matches the regex"""
        log = open(os.path.expanduser('~/.config/pianobar/out'), 'r')
        time_stamp = log.read()[-12:-1]
        log.close()
        if re.match(r'^\d{2}:\d{2}/\d{2}:\d{2}$', time_stamp):
            return (time_stamp, True)
        elif tries < 3:
            verboseprint('FAILED REGEX:', tries, time_stamp)
            verboseprint('Trying again')
            time.sleep(1)
            return self._get_time(tries+1)
        else:
            verboseprint('out of tries')
            return (time_stamp, False)


class playerctl:
    name = 'playerctl'
    system_prefix = arguments['test_mode_prefix']
    system_suffix = arguments['test_mode_suffix']

    def __init__(self):
        verboseprint('playerctl is being inited')
        self.system_prefix = arguments['test_mode_prefix']
        self.system_suffix = arguments['test_mode_suffix']
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
    if arguments['player'] is not None:
        try:
            output = {
                'mpd': mpd,
                'mpc': mpd,
                'pianobar': pianobar,
                'pianoctl': pianobar,
                'playerctl': playerctl,
                'mpris': playerctl,
            }[arguments['player']]()
        except KeyError:
            warning('Invalid player')
            exit(1)
    else:
        list_of_process_names = process.get_comms()

        verboseprint(list_of_process_names)

        # pianobar get priority over mpd, unless mpd is playing.
        if 'mpd' in list_of_process_names:
            if 'pianobar' in list_of_process_names:
                if os.system("mpc status | grep playing &>/dev/null") == 0:
                    output = mpd()
                else:
                    output = pianobar()
            else:
                output = mpd()
        elif 'pianobar' in list_of_process_names:
            output = pianobar()
        else:
            output = playerctl()

    return output


def main(arguments):
    verboseprint('main() starting')
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
