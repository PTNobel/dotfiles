#!/usr/bin/env bash
#
#


# The below comment will check for python3, and launch the script accordingly
''':'

if python --version | grep ' 3.' >/dev/null; then
  python=python
elif which python3 >/dev/null; then
  python=python3
else
  echo No version of python3 found.
  exit 1
fi

if ! [[ -x /usr/local/bin/update_tools_helper ]]; then
  echo "uth not found: update.sh will not function"
fi

exec $python $0

'exit'''

# print('Switched to python')

exit()
