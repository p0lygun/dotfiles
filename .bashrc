#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
alias dotfile='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
alias dotmake='sudo make clean install'
