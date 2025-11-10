!/bin/bash

# Scriptillä ladataan git repo ja siirretään repon index.html tiedosto
# juureen, mistä Nginx-hakee staattisen html-tiedot
# siirrä tämä juureen /home/<oma_tunnus>/<repo-kansio>/

# vaihda tähän kotikansiosi
cd /home/<oma_tunnus>/<repo-kansio>/

git pull

# siirtää tiedoston juureen, josta Nginx hakee staattisen html-tiedoston
sudo mv ~/<repo-kansio>/index.html /var/www/html/index.html
