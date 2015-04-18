#!/bin/bash
#
# launches mutt correctly.

if pidof mutt >/dev/null; then
    mutt -R "$@"
else mutt "$@"
fi
