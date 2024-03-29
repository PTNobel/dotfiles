#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bash.py
#
#  Copyright 2014 Parth Nobel <pnob99@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from os import system
exit_code = False


def bash():
    return system("bash -c 'echo -ne \"\033c\" && bash'")

while exit_code != 37 and exit_code != 42:
    system('echo -ne "\033c"')
    exit_code = bash() % 255

system('echo -ne "\033c"')
exit(0)
