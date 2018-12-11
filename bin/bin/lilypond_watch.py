#!/usr/bin/python3

import os
import sys
import subprocess
import time
from typing import List, Tuple, Dict, Any, Callable, NewType

import shared_watch
from shared_watch import Build

ProcessedArgs = Dict[str, Any]
Recipe = NewType("Recipe", Dict[str, Any])
MainForFileMethod = Callable[[ProcessedArgs], None]
FilePair = Tuple[MainForFileMethod, ProcessedArgs]


def usage(exit_code: int, name: object) -> None:
    usage_text: str = "".join([
        f"Usage: {name} [--help|-h]",
        " [--auxdir </tmp/$USER-LilyPond>|-a </tmp/$USER-LilyPond>]",
        " <file.tex>"])

    if exit_code == 0:
        print(usage_text)
    elif exit_code > 0:
        print(usage_text, file=sys.stderr)
    elif exit_code < 0:
        usage(exit_code, name)
    exit(exit_code)


class LilyPondBuild(Build):
    latexArgs: List[str]

    def __init__(self, recipe: Recipe) -> None:
        self.recipe: Recipe = recipe

        self.pdfname = os.path.join(
            # ''[:: -1] reverses a string. So this reverses the filename, in
            # order to replace the last tex with pdf
            recipe['auxdir'],
            os.path.basename(
                recipe['file'][:: -1].replace('yl.', 'fdp.', 1)[:: -1]
            )
        )

        self.build_steps.append(self.lilypond)

        if recipe['extra_files']:
            for i in recipe['extra_files']:
                self.addWatchedFile(i)

        if recipe['make']:
            self.build_steps = [self.make]

    def lilypond(self):
        print("Call reached", ['lilypond', '-o', self.pdfname[:-4],
              self.recipe['file']])
        subprocess.call(['lilypond', '-o', self.pdfname[:-4],
                        self.recipe['file']])

    def make(self):
        subprocess.call(['make'])


def processargs(input_argv: List[str]) -> ProcessedArgs:
    processingArgs = shared_watch.ProcessArgs(
            input_argv,
            usage,
            LilyPondBuild,
            "LilyPond"
            )

    return processingArgs.render_processargs()


def main_for_file(args: ProcessedArgs) -> None:
    os.makedirs(os.path.expandvars(args['auxdir']), exist_ok=True)

    swapWatch = shared_watch.SwapFilesWatch(
        [args['file']] + args['extra_files']
    )

    args['build'].build()
    if not args['disable_viewer']:
        subprocess.call(['rifle', args['build'].pdfname])
    if os.getenv('VIM', False):
        return

    while swapWatch.swapFilesExist():
        try:
            if args['build'].hasAnythingChanged():
                args['build'].build()
            time.sleep(5)
        except KeyboardInterrupt:
            args['build'].build()

    if args['build'].hasAnythingChanged():
        args['build'].build()
        if swapWatch.swapFilesExist():
            main_for_file(args)


if __name__ == '__main__':
    main_for_file(processargs(sys.argv))
