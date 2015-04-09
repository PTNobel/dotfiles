#!/usr/bin/python3

# A python3 port of musicctl.sh.

from os import system
from sys import argv, stderr


def warning(*objs, prefix='WARNING: '):
    printed_list = str(prefix)
    for i in objs:
        printed_list += i
    print(printed_list, file=stderr)


def usage(exit_code, name_of_program='musicctl.py'):
    usage_text = "Usage: " + name_of_program + \
        " {[a command]|player|commands|usage|help}"
    if exit_code == 0:
        print(usage_text)
    elif exit_code > 0:
        warning(usage_text, prefix='')
    else:
        exit_code = abs(exit_code)
    exit(exit_code)


def verboseprint(*args):
    return
verboseprint('Is null')


# Try to lower the mccabe of this function, perhaps a switch-case hack? Or a
# dictionary?
def processargs(input_argv):
    indexes_to_ignore = list()
    long_args_to_disc = {'--help': 'help', '--verbose': 'verbose',
                         '--trial': 'trial'}
    short_args_to_disc = {'h': 'help', 'v': 'verbose',
                          't': 'trial'}
    output = {"verbose": None, "input": None, 'test_mode_prefix': '',
              'test_mode_suffix': ' >/dev/null'}
    discovered_args = list()
    output["name"] = input_argv[0]
    if len(input_argv) == 1:
        warning("Not enough arguments")
        usage(1, output["name"])
    else:
        for i in range(1, len(input_argv)):
            if i in indexes_to_ignore:
                continue

            elif input_argv[i] == '-':
                    break

            elif input_argv[i][0] == '-':
                verboseprint("Argument found:", input_argv[i],
                             "Index is:", i)
            elif input_argv[i][0:1] == '--':
                try:
                    discovered_args.append(
                        long_args_to_disc[input_argv[i]])
                except KeyError:
                    warning("Invalid argument", prefix='')
                    usage(1, output["name"])

            elif input_argv[i][0] == '-' and input_argv[i][1] != '-':
                for j in range(1, len(input_argv[i])):
                    try:
                        discovered_args.append(
                            short_args_to_disc[input_argv[i][j]])
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
    for i in discovered_args:
        if i == 'help':
            usage(0, output["name"])
        elif i == "verbose":
            output["verbose"] = True
            output["test_mode_suffix"] = ''
        elif i == "trial":
            output["test_mode_prefix"] = 'echo '
            output["test_mode_suffix"] = ''
    return output


if processargs(argv)["verbose"]:
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
    for i in sorted(list(command_dict)):
        print("For player " + i + " the following commands are available:")
        for j in sorted(list(command_dict[i])):
            print("   " + j)
    usage(-1, '')


def main(raw_argv):
    # Arguments is being defined here to insure it's available for the first
    # usage call.
    arguments = processargs(raw_argv)
    verboseprint(arguments)
    # Handle help and usage correctly:
    if arguments["input"] == "usage" or arguments["input"] == "help":
        usage(0, arguments["name"])

    # Figure out what player is running.
    if system("pidof mpd >/dev/null") == 0:
        # pianobar get priority over mpd, unless mpd is playing.
        if system("pidof pianobar >/dev/null") == 0:
            if system("mpc status | grep playing &>/dev/null") == 0:
                player = "mpd"
            else:
                player = "pianobar"
        else:
            player = "mpd"
    elif system("pidof pianobar >/dev/null") == 0:
        player = "pianobar"
    else:
        # - value for usage, because there's no need to print how to use the
        # program when there's no player.
        warning("No music player found")
        usage(-1, arguments["name"])
    verboseprint(player)
    if arguments["input"] == "player":
        print(player)
        usage(-1, arguments['name'])
    # Create a two dimensional dictionary. first key specifies player and the
    # second one is the specific command. It'll be the command to pass to
    # system(). It's possible to define commands that are specific to a
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
    if arguments["input"] == "commands":
        get_keys(commands)
    # Catching a KeyError should prevent this from exploding over the user
    # giving invalid input, though it also prevents bad players from being
    # spotted. So make sure all new players are followed by thorough testing, or
    # just make sure you use the same spelling everywhere.
    try:
        verboseprint(commands[player][arguments["input"]])
        verboseprint(arguments['test_mode_prefix']
                     + commands[player][arguments["input"]]
                     + arguments['test_mode_suffix'])
        system(arguments['test_mode_prefix']
               + commands[player][arguments["input"]]
               + arguments['test_mode_suffix'])
    except KeyError:
        warning("Invalid input.")
        usage(1, arguments["name"])


if __name__ == "__main__":
    main(argv)
