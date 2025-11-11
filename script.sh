#!/bin/bash

# Scriptillä ladataan git repo ja siirretään repon index.html tiedosto
# juureen, mistä Nginx-hakee staattisen html-tiedot

# vaihda tähän kotikansiosi
cd /home/ubuntu/Linux-Repo/

git pull

# siirtää päivitetyt tiedoston oikeisiin paikkoihin
sudo mv ~/Linux-Repo/index.html /var/www/html/index.html
sudo mv ~/Linux-Repo/app.py ~/lemp-app/app.py
