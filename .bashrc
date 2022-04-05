#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export EDITOR=vim;
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
alias dotfile='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
alias dotmake='sudo rm config.h && sudo make clean install'
if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
  exec startx
  # Could use xinit instead of startx
  #exec xinit -- /usr/bin/X -nolisten tcp vt7
fi

