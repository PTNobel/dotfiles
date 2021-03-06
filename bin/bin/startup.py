#!/usr/bin/python3

import os
import sys
import datetime as dt
import time
import process
import i3exit


def warning(*objs):
    """Usage: warning(as, many, objects, as, desired)
    Will print everything passed to it to stderr with the prefix WARNING:"""
    printed_list = 'WARNING'
    for i in objs:
        printed_list += ': '
        printed_list += str(i)
    print(printed_list, file=sys.stderr)


def processargs(argv):
    """Usage: processargs(argv), where argv is a list() of arguments, example,
    sys.argv.
    processargs() goes through argv and returns a dictionary that specifies
    whether the associated flag was passed."""
    output = {"weekly": None, "verbose": None,
              "bootstrap": None, "force": None, 'try-full-boot': False}
    for i in argv:
        if i == "-v" or i == "--verbose":
            output["verbose"] = True
        elif i == "-b":
            output["bootstrap"] = True
        elif i == "-f":
            output["force"] = True
        elif i == "-w":
            output["weeky"] = True
        elif i == "-a":
            output["try-full-boot"] = True
    return output

arguments = processargs(sys.argv)


if arguments["verbose"]:
    def verboseprint(*args):
        """Usage: verboseprint(as,  many, objects, as, desired)
        verboseprint() finctions similarly to warning() accept it only exists if
        arguments["verbose"] is true, or when -v is present. It is intended to
        dump objects into stdout."""
        for arg in args:
            print(arg)
else:
    def verboseprint(*args):  # do-nothing function
        return


def are_there_other_startuppy():
    """Begin checking to make sure this is the only version of startup.py to be
    running. This helps fight issues with multiple instances of startup.py
    launching processes repeatedly."""
    def check_if_pid_is_startuppy(pidnum):
        return "startup" in \
            process.get_cmdline_of_pid(pidnum)[1] \
            and "python" in \
            process.get_cmdline_of_pid(pidnum)[0]

    process.update_buffers()
    pids = process.get_pids()
    pids.remove(str(os.getpid()))
    verboseprint(pids)
    verboseprint(str(os.getpid()))

    if os.getpid() in pids:
        verboseprint(
            'Something\'s weird... pids containts os.getpid()',
            pids,
            os.getpid())
        exit(255)

    for pid in pids:
        try:
            verboseprint(pid)
            if pid == str(os.getpid()):
                print('This script')
            verboseprint(process.get_cmdline_of_pid(pid))
            while check_if_pid_is_startuppy(pid):
                warning("Is there another " + os.path.basename(sys.argv[0]) +
                        " running?")
                time.sleep(60)
            else:
                verboseprint(pid + " is not startup.py")
        except (IOError, IndexError):  # proc has already terminated
            verboseprint(pid + " has terminated, or has no args")
            continue


def clean_list(input_list):
    """removes unnecessary characters from a list."""
    output_list = list()
    for i in input_list:
        var = i.replace('\n', '')
        output_list.append(var)
    return output_list


def update_log(log):
    """writes today's date to a log file."""
    today = str(dt.date.today())
    log_file_writeable = open(log, 'w')
    log_file_writeable.write(today)
    log_file_writeable.close()


def success(commands, run_log_str):
    """Iterates through the list commands, and executes the commands. It then
    creates run_log_str in /tmp/"""
    verboseprint(commands)
    for i in commands:
        verboseprint(i)
        if os.system('urxvt -e exit') != 0:
            warning('Something\'s very wrong with this X server')
            warning('Dazed and confused and quitting now')
            exit(6)
        os.system(i + ' >/dev/null &')
    run_log = open('/tmp/' + run_log_str, mode='w')
    run_log.write('We finished.\n')
    run_log.close()


def main(arguments):
    # Wait for all other startup.py instances to exit, so a lockfile will be
    # in place when we check for it.
    are_there_other_startuppy()

    # Variable definitions this should cover everything.
    date_log = os.path.expanduser("~/.parth/date.log")
    autostart = os.path.expanduser("~/.i3/autostart")
    bootstrap = os.path.expanduser("~/.i3/bootstrap")
    week = os.path.expanduser("~/.i3/weekly_tasks")
    date_log_file = open(date_log, 'r')
    log_value = date_log_file.read()
    date_log_file.close()
    today = str(dt.date.today())
    current_hour = int(str(dt.datetime.now().time())[0:2])
    autostart_file_list = open(autostart, 'r')
    bootstrap_file_list = open(bootstrap, 'r')
    weekly_file_list = open(week, 'r')
    run_log_name = "startup." + os.getenv('DISPLAY', '')[1:] + '.log'

    raw_commands = autostart_file_list.readlines()
    raw_bootstarp_commands = bootstrap_file_list.readlines()
    raw_weekly = weekly_file_list.readlines()
    raw_commands += raw_bootstarp_commands

    command_list = clean_list(raw_commands)
    bootstrap_commands = clean_list(raw_bootstarp_commands)
    weekly = clean_list(raw_weekly)

    if os.system('urxvt -e exit') != 0:
        warning('Something\'s very wrong with this X server')
        warning('Dazed and confused and quitting now')
        os.system('dmesg >/tmp/dmesg.X.' + os.getenv('DISPLAY', '')[1:] +
                  '.log')
        exit(5)

    elif arguments["force"]:
        success(command_list, run_log_name)

    elif arguments["bootstrap"]:
        success(bootstrap_commands, run_log_name)

    elif arguments["weekly"]:
        command_list += weekly
        success(command_list, run_log_name)

    elif run_log_name in os.listdir('/tmp')and not arguments["try-full-boot"]:
        warning('Already ran')
        exit(8)

    elif current_hour >= 22 or current_hour <= 6:
        success(bootstrap_commands, run_log_name)

    elif not i3exit.which_output()[1]:
        success(bootstrap_commands, run_log_name)

    elif log_value != today:
        if dt.date.today().weekday() == 5:
            command_list += weekly
        update_log(date_log)
        success(command_list, run_log_name)

    else:
        success(bootstrap_commands, run_log_name)

    exit(0)


if __name__ == "__main__":
    main(arguments)
