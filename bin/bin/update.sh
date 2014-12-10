#!/bin/bash

backup.sh ; sudo dash -c 'echo "updating pkgfile database" && pkgfile -u && echo "updating mlocate database" && updatedb  && echo "updating man database" && mandb' | lolcat
