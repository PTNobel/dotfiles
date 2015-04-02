#!/usr/bin/python3

import os
import sys
import mimetypes


def warning(*objs, prefix='WARNING: '):
    printed_list = str(prefix)
    for i in objs:
        printed_list += i
    print(printed_list, file=sys.stderr)


def usage(exit_code, name_of_program):
    usage_text = "Usage: " + name_of_program + \
        " {commands|usage|help}"
    if exit_code == 0:
        print(usage_text)
    elif exit_code > 0:
        warning(usage_text, prefix='')
    else:
        exit_code = abs(exit_code)
    exit(exit_code)


def processargs(argv):
    indexes_to_ignore = list()
    supported_arguments = ['-h', '--help', '-v', '--verbose']
    output = {"verbose": None, "file": list()}
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
                    verboseprint("Argument found:", argv[i], "Index is:", i)
                    if argv[i] not in supported_arguments:
                        warning("Invalid argument", prefix='')
                        usage(1, output["name"])

                    else:
                        if argv[i] == '-h' or argv[i] == '--help':
                            usage(0, output["name"])
                        elif argv[i] == "-v" or argv[i] == "--verbose":
                            output["verbose"] = True

                else:
                    output["file"].append(argv[i])

    if output["file"] == []:
        warning("Error parsing arguments")
        verboseprint(
            output,
            argv,
            i,
            argv[i],
            output["file"])
        usage(1, output["name"])

    return output


if '-v' in sys.argv or '--verbose' in sys.argv:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to stuff
        # everything to be printed into a string.
        for arg in args:
            print(arg)


else:
    def verboseprint(*args):
        return


def get_file_type(file):
    type = mimetypes.guess_type(file, strict=True)
    return type


def x_is_running(file):
    type = get_file_type(file)
    verboseprint(type)
    return


def x_is_not_running(file):
    type = get_file_type(file)
    verboseprint(type)
    return


def main(raw_argv):
    arguments = processargs(raw_argv)
    verboseprint(arguments)

    if "DISPLAY" in os.environ:
        for i in arguments["files"]:
            x_is_running(i)

    else:
        for i in arguments["files"]:
            x_is_not_running(i)


if __name__ == "__main__":
    main(sys.argv)
