#!/bin/bash

APPDIR=/usr/share/PinephoneHacks

echo -e "\e[33m [ Checking for previous versions]\e[0m"
if [ -d "$APPDIR" ]; then
    rm -rf $APPDIR
fi

echo -e "\e[32m [ Installing Pinephone Hacks ]\e[0m"
mkdir $APPDIR
cp main.py $APPDIR
cp PinephoneHacks.css $APPDIR
cp PinephoneHacks.png $APPDIR
cp PinephoneHacks.desktop /usr/share/applications/
cp org.freedesktop.policykit.PinephoneHacks.policy /usr/share/polkit-1/actions/
