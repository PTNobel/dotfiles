#!/usr/bin/python3

import process
import sys
import subprocess


def main():
    def processargs():
        output = dict()
        for i in sys.argv[1:]:
            print(i)

            if '--' in i:
                raise NotImplementedError

            elif '-' in i:
                raise NotImplementedError

            else:
                output["procname"] = i

        return output

    args = processargs()

    for i in process.get_pids_of_comm('bash') + \
            process.get_pids_of_comm('/bin/bash') + \
            process.get_pids_of_comm('/usr/bin/bash'):
        print(i)
        try:
            if args["procname"] == process.get_cmdline_of_pid(i)[1]:
                kill(i)
        except IndexError:
            continue


def kill(i: str):
    print(i)
    subprocess.call(["kill", i])

if __name__ == '__main__':
    main()
