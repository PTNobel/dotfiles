#!/usr/bin/python3

import latex_watch
import pandoc_watch
import sys

for arg in sys.argv:
    if '.md' in arg:
        pandoc_watch.main_for_file(pandoc_watch.processarg(sys.argv))

    elif '.tex' in arg:
        latex_watch.main_for_file(latex_watch.processarg(sys.argv))

# No arguments given
if len(sys.argv) == 1:
    # Find open file
    pass
