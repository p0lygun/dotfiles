#!/bin/bash
#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
  exec startx
  # Could use xinit instead of startx
  #exec xinit -- /usr/bin/X -nolisten tcp vt7
fi

export EDITOR=helix;
alias ls='ls --color=auto'
alias dotfile='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
alias dotmake='sudo rm config.h && sudo make clean install'
alias p='sudo pacman'
PS1='\n\[\e[0;90m\][ \[\e[0;1;32m\]\u\[\e[0;38;5;245m\]@\[\e[0;2;38;5;247m\]\H \[\e[0;90m\]]\[\e[0;2;38;5;78m\]$(~/.config/scripts/prompt_info.sh)\[\e[0m\]\n\[\e[0;90m\][\[\e[0;4;36m\]\w\[\e[0;2;38;5;168m\] $(git branch 2>/dev/null | grep '"'"'^*'"'"' | colrm 1 2)\[\e[0;90m\]] \[\e[0;31m\] \n$ \[\e[0m\]'
neofetch

