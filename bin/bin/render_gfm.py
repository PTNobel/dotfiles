#!/usr/bin/python3

import sys
import gfm

fd = open(sys.argv[1])

in_file_content = fd.readlines()
out_file_content = list()

for line in in_file_content:
    if '|ADDGFM|' in line:
        words = line.strip().split('|')
        out_file_content.append(
            '  gmm        = ' +
            str(gfm.gfm_of_whole(words[2])) +
            ' ,\n')

    else:
        out_file_content.append(line)

out_fd = open('new_' + sys.argv[1], 'w')
out_fd.writelines(out_file_content)
out_fd.close()
