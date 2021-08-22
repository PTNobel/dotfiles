#!/usr/bin/python3

import latex_watch
import pandoc_watch
import lilypond_watch
import sys
import os
from threading import Thread
from typing import List, Tuple, Dict, Any, Callable

ProcessedArgs = Dict[str, Any]
MainForFileMethod = Callable[[ProcessedArgs], None]
FilePair = Tuple[MainForFileMethod, ProcessedArgs]


def is_swap_in_cur_dir(swap_file: str, cur_dir: List[str]) -> bool:
    return any(
        (
            os.path.samefile(swap_file[:-4].replace('%', '/'), (file_name))
            for file_name in cur_dir
        )
    )


def processargs(
        argv: List[str],
        ) -> List[FilePair]:
    output: List[FilePair] = list()
    dashArguments = False
    markdownFiles = False
    latexFiles = False
    lilypondFiles = False
    # Skip the name of the program
    for arg in argv[1:]:
        if arg[0] == '-':
            dashArguments = True
        elif '.md' in arg[-3:]:
            markdownFiles = True
        elif '.tex' in arg[-4:]:
            latexFiles = True
        elif '.ly' in arg[-3:]:
            lilypondFiles = True

    if not dashArguments and len(argv) > 1:
        for arg in argv[1:]:
            if '.md' in arg[-3:]:
                output.append(
                        (
                            pandoc_watch.main_for_file,
                            pandoc_watch.processargs([argv[0], arg])
                        )
                )

            elif '.tex' in arg[-4:]:
                output.append(
                        (
                            latex_watch.main_for_file,
                            latex_watch.processargs([argv[0], arg])
                        )
                )
            elif '.ly' in arg[-3:]:
                output.append(
                        (
                            lilypond_watch.main_for_file,
                            lilypond_watch.processargs([argv[0], arg])
                        )
                )

    elif len([i for i in [markdownFiles, latexFiles, lilypondFiles] if i]) > 1:
        exit(1)
    elif markdownFiles:
        output.append(
                (
                    pandoc_watch.main_for_file,
                    pandoc_watch.processargs(argv)
                )
        )

    elif latexFiles:
        output.append(
                (
                    latex_watch.main_for_file,
                    latex_watch.processargs(argv)
                )
        )

    elif lilypondFiles:
        output.append(
                (
                    lilypond_watch.main_for_file,
                    lilypond_watch.processargs(argv)
                )
        )

    else:
        output += find_files(argv)
    return output


def find_files(argv: List[str]):
    output: List[str] = list()
    cur_dir: List[str] = [os.path.realpath(f) for f in os.listdir()]
    # No file name given
    for file_name in os.listdir():
        if len(file_name) > 9 and file_name[0] == '.' and \
                file_name[-8:] == '.tex.swp':
                output.append(
                    (
                        latex_watch.main_for_file,
                        latex_watch.processargs(argv + [file_name[1:-4]]))
                )
        if len(file_name) > 8 and file_name[0] == '.' and \
                file_name[-7:] == '.md.swp':
            output.append(
                    (
                        pandoc_watch.main_for_file,
                        pandoc_watch.processargs(argv + [file_name[1:-4]])
                    )
            )
        if len(file_name) > 8 and file_name[0] == '.' and \
                file_name[-7:] == '.ly.swp':
            output.append(
                    (
                        lilypond_watch.main_for_file,
                        lilypond_watch.processargs(
                            argv + [file_name[1:-4]])
                    )
            )
    for file_name in os.listdir(os.path.expanduser('~/.cache/vim/swap')) + \
            os.listdir(os.path.expanduser('~/.local/share/nvim/swap')):
        if len(file_name) > 8 and file_name[-8:] == '.tex.swp' \
                and is_swap_in_cur_dir(file_name, cur_dir):
                output.append(
                    (
                        latex_watch.main_for_file,
                        latex_watch.processargs(argv + [
                            os.path.relpath(file_name[:-4].replace('%', '/'))
                        ])
                    )
                )
        if len(file_name) > 7 and file_name[-7:] == '.md.swp' \
                and is_swap_in_cur_dir(file_name, cur_dir):
            output.append(
                    (
                        pandoc_watch.main_for_file,
                        pandoc_watch.processargs(argv + [
                            os.path.relpath(file_name[:-4].replace('%', '/'))
                        ])
                    )
            )
        if len(file_name) > 7 and file_name[-7:] == '.ly.swp' \
                and is_swap_in_cur_dir(file_name, cur_dir):
            output.append(
                    (
                        lilypond_watch.main_for_file,
                        lilypond_watch.processargs(argv + [
                            os.path.relpath(file_name[:-4].replace('%', '/'))
                        ])
                    )
            )
    return output


def launchWatches(mainsAndArgs: List[FilePair]) -> None:
    if len(mainsAndArgs) == 1:
        mainsAndArgs[0][0](mainsAndArgs[0][1])

    else:
        for mainAndArgPair in mainsAndArgs:
            Thread(
                target=mainAndArgPair[0],
                args=tuple([mainAndArgPair[1]]),
                ).start()


if __name__ == '__main__':
    launchWatches(processargs(sys.argv))
