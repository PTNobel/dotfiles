# If not running interactively, don't do anything
[[ $- != *i* ]] && return


if [ $UID = 0 ]
then export PS1="\[\e[00;37m\][\[\e[0m\]\[\e[01;31m\]\u@\h\[\e[0m\]\[\e[00;37m\] \[\e[0m\]\[\e[01;36m\]\W\[\e[0m\]\[\e[00;37m\]]\\$ \[\e[0m\]"
else export PS1="\[\e[00;37m\][\[\e[0m\]\[\e[01;32m\]\u@\h\[\e[0m\]\[\e[00;37m\] \[\e[0m\]\[\e[01;36m\]\W\[\e[0m\]\[\e[00;37m\]]\\$ \[\e[0m\]"
fi
if [ "$LD_PRELOAD" == "libfakeroot.so" ]
then export PS1="\[\e[00;37m\][\[\e[0m\]\[\e[01;32m\]\u@\h\[\e[0m\]\[\e[00;37m\] \[\e[0m\]\[\e[01;36m\]\W\[\e[0m\]\[\e[00;37m\]]\\$ \[\e[0m\]"
fi
# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.
#echo bashrc
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
#echo bash_alaises
# functions
# cd and ls in one
cl() {
    dir=$1
    if [[ -z "$dir" ]]; then
        dir=$HOME
    fi
    \cd "$dir" && ls    
#    if [[ -d "$dir" ]]; then
#        \cd "$dir"
#        ls
#    else
#        echo "bash: cl: '$dir': Directory not found"
#    fi
}
# extract files
extract() {
    local c e i

    (($#)) || return

    for i; do
        c=''
        e=1

        if [[ ! -r $i ]]; then
            echo "$0: file is unreadable: \`$i'" >&2
            continue
        fi

        case $i in
            *.t@(gz|lz|xz|b@(2|z?(2))|a@(z|r?(.@(Z|bz?(2)|gz|lzma|xz)))))
                   c=(bsdtar xvf);;
            *.7z)  c=(7z x);;
            *.Z)   c=(uncompress);;
            *.bz2) c=(bunzip2);;
            *.exe) c=(cabextract);;
            *.gz)  c=(gunzip);;
            *.rar) c=(unrar x);;
            *.xz)  c=(unxz);;
            *.zip) c=(unzip);;
            *)     echo "$0: unrecognized file extension: \`$i'" >&2
                   continue;;
        esac

        command "${c[@]}" "$i"
        ((e = e || $?))
    done
    return "$e"
}



man() {
    env LESS_TERMCAP_mb=$'\E[01;31m' \
    LESS_TERMCAP_md=$'\E[01;38;5;74m' \
    LESS_TERMCAP_me=$'\E[0m' \
    LESS_TERMCAP_se=$'\E[0m' \
    LESS_TERMCAP_so=$'\E[38;5;246m' \
    LESS_TERMCAP_ue=$'\E[0m' \
    LESS_TERMCAP_us=$'\E[04;38;5;146m' \
    man "$@"
}

#place for anything like exports etc.
PATH=/home/parth/bin:$PATH
source /usr/share/doc/pkgfile/command-not-found.bash
export VISUAL=vim
export EDITOR=vim
shopt -s cdspell autocd
export BROWSER=firefox
export PAGER=vimpager
eval "$(beet completion)"
