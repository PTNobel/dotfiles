#!/bin/bash

if pidof mutt >/dev/null; then
		mutt -R "$@"
else mutt "$@"
fi
