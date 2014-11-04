## Modified commands ## {{{
alias less='less --quiet'
alias diff='colordiff'              # requires colordiff package
alias grep='grep --color=auto'
alias more='less'
alias df='df -h'
alias du='du -c -h'
alias mkdir='mkdir -p -v'
alias nano='nano -w'
alias dmesg='dmesg -HL'
# }}}

## New commands ## {{{
alias da='date "+%A, %B %d, %Y [%T]"'
alias du1='du --max-depth=1'
alias hist='history | grep'         # requires an argument
alias openports='ss --all --numeric --processes --ipv4 --ipv6'
alias pgg='ps -Af | grep'           # requires an argument
alias ..='cd ..'
alias open=gvfs-open
# }}}

# Privileged access
if [ $UID -ne 0 ]; then
    alias sudo='sudo '
    alias scat='sudo cat'
    alias slolcat='sudo lolcat'
    alias svim='sudoedit'
    alias root='sudo -s'
    alias reboot='systemctl reboot'
    alias poweroff='systemctl poweroff'
    alias update='yaourt -Syua'
    alias netctl='sudo netctl'
    alias wifi-menu='sudo wifi-menu'
fi

## ls ## {{{
alias ls='ls -hF --color=auto'
alias lr='ls -R'                    # recursive ls
alias ll='ls -l'
alias la='ls -A'
alias lla='ll -A'
alias lx='ll -BX'                   # sort by extension
alias lz='ll -rS'                   # sort by size
alias lt='ll -rt'                   # sort by date
alias lm='la | more'
# }}}

## Safety features ## {{{
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -I'                    # 'rm -i' prompts for every file
# safer alternative w/ timeout, not stored in history
#alias rm=' timeout 3 rm -Iv --one-file-system'
alias ln='ln -i'
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'
alias cls=' echo -ne "\033c"'       # clear screen for real (it does not work in Terminology)
# }}}

## Make Bash error tolerant ## {{{
alias :q=' exit'
alias :Q=' exit'
alias :x=' exit'
alias cd..='cd ..'
# }}}

alias up='cd ..'
alias pacman='pacman --color=auto'
alias free='free -h'
alias suod='sudo'
alias rhythmbox='setsid rhythmbox'
alias firefox='setsid firefox'
alias conky='setsid conky'
alias geany='setsid geany'
alias file-roller='setsid file-roller'
alias x="setsid env DISPLAY=:0 "
alias root-shell="sudo bash -c 'reset ; cd /root ; /home/parth/bin/bash.py';exit"
alias xdg-open="setsid xdg-open &>/dev/null"
alias gimp='setsid gimp'
alias thunar='setsid thunar'
alias clementine="setsid clementine"
alias fix='sudo \`history -p \!\!\`'
alias cd=cl
alias iceweasel='setsid iceweasel'
alias scan_wifi="iwlist wlo1 scanning | grep ESSID -B 3"
alias watch_journal='journalctl -fe'
