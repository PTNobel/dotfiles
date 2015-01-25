#!/bin/bash
DIR=$1
FILES=$2
#if [ -z "$1" ]; then DIR=755; fi
#if [ -z "$2" ]; then FILES=644; fi
#EXECS=$(($FILES+111))
#echo $EXECS
#find ./ -type d -exec chmod $DIR {} \;
#find ./ -type f -exec chmod $FILES {} \;
chmod +X
#find -type f -name "*.sh" -exec chmod $EXECS {} \;
#find -type f -name "*.py" -exec chmod $EXECS {} \;
#find -type f -name "*.so" -exec chmod $EXECS {} \;
