#!/bin/bash

# Scriptillä ladataan git repo ja siirretään repon index.html tiedosto
# juureen, mistä Nginx-hakee staattisen html-tiedot

# vaihda tähän kotikansiosi
cd /home/ubuntu/<kansio, johon tiedostot ladataan Github:sta>

# vaihda repon tilalle oman reposition osoite
git pull

# siirtää tiedoston juureen, josta Nginx hakee staattisen html-tiedoston
sudo mv <~/repon_nimi/index.html> /var/www/html/index.html
