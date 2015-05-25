#!/usr/bin/python3
#
# A python port of factor from coreutils.
# I made it for fun. It performs horribly.
#

from sys import argv

if len(argv) != 2:
    exit(1)
i = 2
factors = list()
try:
    orig_num_to_factor = int(argv[1])
    if float(argv[1]) != float(orig_num_to_factor):
        print("factor: ‘" + argv[1] + "’ is not a valid positive integer")
        exit(1)
    elif orig_num_to_factor < 0:
        print("factor: ‘" + argv[1] + "’ is not a valid positive integer")
        exit(1)
except ValueError:
    print("factor: ‘" + argv[1] + "’ is not a valid positive integer")
    exit(1)
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
