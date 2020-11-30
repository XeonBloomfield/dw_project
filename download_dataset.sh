#!/bin/bash

mkdir dataset -p
wget http://blzdistsc2-a.akamaihd.net/ReplayPacks/3.16.1-Pack_1-fix.zip
unzip 3.16.1-Pack_1-fix.zip -d dataset
rm 3.16.1-Pack_1-fix.zip
