#!/usr/bin/python3
#
# A python port of factor from coreutils.
# I made it for fun.
#

import sys

if len(sys.argv) != 2:
    exit(1)
i = 2
factors = list()
orig_num_to_factor = int(sys.argv[1])
num_to_factor = orig_num_to_factor
while i * i < orig_num_to_factor:
    while int(num_to_factor % i) == 0:
        num_to_factor = num_to_factor / i
        factors.append(i)
    i = i + 1
if num_to_factor != 1:
    factors.append(int(num_to_factor))

string_to_print = str(orig_num_to_factor) + ": "
for i in factors:
    string_to_print += str(i) + ' '

print(string_to_print[0:-1])
