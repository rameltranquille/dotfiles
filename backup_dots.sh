#!/bin/sh

mkdir -p ~/dotfiles/
HOME="/home/ramel"

dotfiles="$HOME/.bashrc $HOME/.vimrc $HOME/.xinitrc $HOME/.taskrc $HOME/.config/dmenu $HOME/.config/alacritty/alacritty.yml $HOME/.config/picom/ $HOME/.config/qtile/ $HOME/.config/spotifyd/ $HOME/.config/spotify-tui/ $HOME/.config/newsboat/"

for dir in $dotfiles; do
	cp -rf $dir ~/dotfiles/
done

git add .
git commit -m 'normal backup'
git push -u origin main

