#!/usr/bin/python3
#
# Add a processargs(), warning(), and verboseprint()
#

import sys
import os
import time


def usage():
    return


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)


def processargs(argv):
    for i in range(1, len(argv)):
        if i == "-h":
            usage()
        if i == "-v" or i == "--verbose":
            VERBOSE = True
        elif i == "-l":
            STATE_l = True
    return {"VERBOSE": VERBOSE, "l": STATE_l}

arguements = processargs()

if arguements["VERBOSE"]:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to
        # stuff everything to be printed into a single string
        for arg in args:
            print(arg)
else:
    def verboseprint(*args):
        return


user_input = str()


if len(sys.argv) == 1:
    user_input = input("What do you want to say? ")
else:
    for i in range(1, len(sys.argv)):
        user_input += sys.argv[i]

final_output = str()

for i in user_input:
    if i == ' ':
        final_output += " space "
    elif i == '\'':
        final_output += " apostrophe "
    elif i == '"':
        final_output += " quotedbl "
    elif i == '`':
        final_output += " grave "
    elif i == '~':
        final_output += " asciitilde "
    elif i == '!':
        final_output += " exclam "
    elif i == '/':
        final_output += " slash "
    elif i == '\\':
        final_output += " backslash "
    else:
        final_output += i + " "

final_output += " Return"

print(final_output)

print("Warning xdotool will be launched in 30 seconds")

time.sleep(30)
xdotool_call = "xdotool key " + final_output
for i in range(0, 5):
    os.system(xdotool_call)
