shopt -s autocd
shopt -s histappend

HISTCONTROL=ignoreboth
HISTSIZE=-1
HISTFILESIZE=-1

# PS1="\[\e[0;37m\][\[\e[0;32m\]\t\[\e[0;37m\]]\[\e[0;32m\]\u\[\e[0;32m\]@\[\e[0;33m\]\w \[\e[0;37m\]> \[\e[0m\]"
export PS1="[\[$(tput sgr0)\]\[\033[38;5;13m\]\T\[$(tput sgr0)\]]\[$(tput sgr0)\]\[\033[38;5;13m\]\u@\[$(tput sgr0)\]\[\033[38;5;10m\]\w\[$(tput sgr0)\]>\[$(tput sgr0)\]"""

if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto --group-directories-first'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias la='ls -A'
alias l='ls -CF'
alias sp='sudo pacman'
alias sps='sudo pacman -S'
alias ex='exit'
alias g='git'
alias ll='ls -l'
alias tda='todo add'
alias tdr='todo rm'
alias tde='todo edit'
alias bpy='bpytop'
alias lutris_perms="sudo sh -c 'sysctl -w abi.vsyscall32=0'"
alias update_dots='cd ~/dotfiles && bash /home/ramel/dotfiles/backup_dots.sh'
alias py='python'
alias stonk='bash ~/scripts/ticker.sh BTC-USD ^GSPC DOW GC=F CL=F ^IXIC'
alias smi='sudo make install'
alias mb='xrandr --output DVI-D-0 --brightness 1 && xrandr --output HDMI-0 --brightness 1'
alias lb='xrandr --output DVI-D-0 --brightness .5 && xrandr --output HDMI-0 --brightness .5'
alias nb='xrandr --output DVI-D-0 --brightness .75 && xrandr --output HDMI-0 --brightness .75'
