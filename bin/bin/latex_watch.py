#!/usr/bin/python3

import os
import sys
import subprocess
import time


def usage(exit_code, name):
    usage_text = "Usage: %s" % name

    if exit_code == 0:
        print(usage_text)
    elif exit_code > 0:
        print(usage_text, file=sys.stderr)
    elif exit_code < 0:
        usage(exit_code, name)
    exit(exit_code)


class Build:
    build_steps = list()

    def __init__(self, recipe):
        self.recipe = recipe
        self.addToBuild('latex')

        if recipe['biber']:
            self.addToBuild('biber')

        if recipe['sagetex']:
            self.addToBuild('sagetex')

        self.addToBuild('latex')

    def latex(self):
        subprocess.call([self.recipe['engine'],
                         '-output-directory',
                         self.recipe['auxdir'],
                         "-interaction=nonstopmode", self.recipe['file']])

    def biber(self):
        subprocess.call(
            ["biber",
             "--output-directory", self.recipe['auxdir'],
                "--input-directory", self.recipe['auxdir'],
                os.path.basename(self.recipe
                                 ['file'][:: -1].replace
                                 ('xet.', '', 1)[:: -1])])

    def sagetex(self):
        firstdir = os.getcwd()
        os.chdir(self.recipe['auxdir'])
        subprocess.call(
            ['sage',
                os.path.basename(self.recipe
                                 ['file'][:: -1].replace
                                 ('xet', 'egas.xetegas', 1)[:: -1])])
        os.chdir(firstdir)

    def build(self):
        for i in self.build_steps:
            i()

    def addToBuild(self, nameOfCompilationStep):
        self.build_steps.append(
            {
                'latex': self.latex,
                'biber': self.biber,
                'sagetex': self.sagetex
            }[nameOfCompilationStep]
        )


def processargs(input_argv):

    # All of these run in the same scope as processargs(). They make changes to
    # output.
    def _help():
        usage(0, output['name'])

    def _sagetex():
        output_recipe['sagetex'] = True

    def _biber():
        output_recipe['biber'] = True

    def _auxdir():
        if '=' in input_argv[i]:
            auxdir = input_argv[i].split('=')[1]
        else:
            auxdir = input_argv[i + 1]
            indexes_to_ignore.append(i + 1)

        output_recipe["auxdir"] = os.path.expandvars(os.path.expanduser(auxdir))
        output["auxdir"] = os.path.expandvars(os.path.expanduser(auxdir))

    def _engine():
        if '=' in input_argv[i]:
            engine = input_argv[i].split('=')[1]
        else:
            engine = input_argv[i + 1]
            indexes_to_ignore.append(i + 1)

        output_recipe["engine"] = engine

    # In place of a switch-case statement the following dictionaires link argv
    # entries to functions.
    long_args_to_disc = {'--help': _help,
                         '--sagetex': _sagetex,
                         '--engine': _engine,
                         '--biber': _biber,
                         '--auxdir': _auxdir,
                         }
    short_args_to_disc = {'h': _help,
                          'b': _biber,
                          'e': _engine,
                          'a': _auxdir,
                          }
    output = {"input": None,
              "name": os.path.basename(input_argv[0]),
              "player": None,
              "build": [],
              'auxdir': os.path.expandvars('/tmp/$USER-LaTeX')
              }

    output_recipe = {
        'engine': 'pdflatex',
        'biber': False,
        'sagetex': False,
        'file': '',
        'auxdir': os.path.expandvars('/tmp/$USER-LaTeX')
    }
    indexes_to_ignore = list()

    if len(input_argv) == 1:
        print("Not enough arguments", file=sys.stderr)
        usage(1, output['name'])
    else:
        # range() starts at 1 to prevent the name from being processed.
        for i in range(1, len(input_argv)):
            if i in indexes_to_ignore:
                continue

            elif len(input_argv[i]) >= 2 and input_argv[i][0:2] == '--':
                try:
                    long_args_to_disc[input_argv[i].split('=')[0]]()
                except KeyError:
                    print("Invalid argument", file=sys.stderr)
                    usage(1, output['name'])

            elif input_argv[i][0] == '-' and input_argv[i][1] != '-':
                for j in range(1, len(input_argv[i])):
                    try:
                        short_args_to_disc[input_argv[i][j]]()
                    except KeyError:
                        print("Invalid argument", file=sys.stderr)
                        usage(1, output['name'])

            elif not output_recipe["file"]:
                output_recipe["file"] = input_argv[i]
                output["file"] = input_argv[i]

            else:
                print("Error parsing arguments", file=sys.stderr)
                usage(1, output['name'])
    output['build'] = Build(output_recipe)
    print(output['build'].build_steps)
    return output

# global arguments
arguments = processargs(sys.argv)


class FileWatch:
    _failed_reads = 0

    def __init__(self, file_name):
        self._file_name = file_name
        self._last_content = self._read_file()

    def _read_file(self):
        try:
            fd = open(self._file_name)
        except FileNotFoundError as e:
            self._failed_reads += 1
            if self._failed_reads <= 5:
                return self._read_file()
            else:
                raise e
            time.sleep(.3)
        filecontents = fd.readlines()
        fd.close()
        return filecontents

    def hasItChanged(self):
        self._failed_reads = 0
        _new_content = self._read_file()
        if _new_content != self._last_content:
            self._last_content = _new_content
            return True
        else:
            return False


def main():
    watchedFile = FileWatch(arguments['file'])
    os.makedirs(os.path.expandvars(arguments['auxdir']), exist_ok=True)
    pdfname = os.path.join(
        # ''[:: -1] reverses a string. So this reverses the filename, in order
        # to replace the last tex with pdf
        arguments['auxdir'], os.path.basename(arguments['file'][:: -1].replace
                                              ('xet', 'fdp', 1)[:: -1]))
    swapfile = os.path.join(os.path.dirname(arguments['file']),
                            '.' + os.path.basename(arguments['file']) + '.swp')
    arguments['build'].build()
    subprocess.call(['rifle', pdfname])
    while os.path.exists(swapfile):
        if watchedFile.hasItChanged():
            arguments['build'].build()
        time.sleep(5)
    arguments['build'].build()


if __name__ == '__main__':
    main()
