shopt -s autocd
shopt -s histappend

HISTCONTROL=ignoreboth
HISTSIZE=-1
HISTFILESIZE=-1

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

PS1="\[\e[0;37m\][\[\e[0;32m\]\t\[\e[0;37m\]]\[\e[0;32m\]\u\[\e[0;32m\]@\[\e[0;33m\]\w \[\e[0;37m\]> \[\e[0m\]"

if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto --group-directories-first'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias la='ls -A'
alias l='ls -CF'
alias do='clear & yokadi t_list'
alias yrm='yokadi t_remove'
alias ya='yokadi t_add'
alias sa='sudo apt'
alias sai='sudo apt install'
alias ex='exit'
alias g='git'
alias ymd='yokadi t_mark_done'
alias btop='bpytop'
alias stonk='./ticker.sh $(cat ~/.ticker.conf)'
alias sc='watch -n 5 -t -c ./ticker.sh $(cat ~/.ticker.conf)'
alias ll='ls -l'
