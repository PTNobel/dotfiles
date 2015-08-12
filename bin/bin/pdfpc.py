#!/usr/bin/env python3

import os
import sys
import json
import subprocess

if len(sys.argv) <= 1:
    exit(1)

os.system('xrandr --output LVDS1 --primary')
encoded_outputs = subprocess.check_output(
    ['i3-msg', '-t', 'get_outputs'], universal_newlines=True)

encoded_workspaces = subprocess.check_output(
    ['i3-msg', '-t', 'get_workspaces'], universal_newlines=True)

outputs = json.loads(str(encoded_outputs))
workspaces = json.loads(str(encoded_workspaces))
pdfpc_call = sys.argv.copy()
pdfpc_call[0] = 'pdfpc'


for output in outputs:
    if output['primary']:
        primary_output = output.copy()
    if output['name'] == 'LVDS1':
        if not output['primary']:
            subprocess.call(['xrandr', '--output', 'LVDS1', '--primary'])


for workspace in workspaces:
    if workspace['focused'] \
            and workspace['output'] is not primary_output['name']:
        pdfpc_call.append('-s')


subprocess.call(pdfpc_call)

print(type(pdfpc_call))
