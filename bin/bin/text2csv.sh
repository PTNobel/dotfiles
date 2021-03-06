#!/bin/bash
# -*- coding: utf-8 -*-
#
#  text2csv.sh
#
#  Copyright 2014 Parth Nobel <parth@parth-laptop>
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

# so here the input should be a file that is read by sed and then sent
# either to stdout OR the file with refined_ added to the front of the
# file. Later versions should be able to make the class_list.py script
#echo "script started"
#echo "iput="$1
#INPUT_FILE=`echo "$1" | sed 's/ /\\\ /g'`
INPUT_FILE="$1"
#echo INPUT_FILE: $INPUT_FILE
#exit
LIST=$(tr '\n' '"' < "$INPUT_FILE" | sed 's/\"/,/g')
LIST_2="${LIST:0:-1}"
echo "$LIST_2"
