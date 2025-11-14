#!/bin/bash

# Scriptillä ladataan git repo ja siirretään
# päivitetyt tiedostot niille kuuluville sijainneille

cd /home/ubuntu/Linux-Repo/
git pull

# siirtää päivitetyt tiedoston oikeisiin paikkoihin
sudo cp ~/Linux-Repo/index.html /var/www/html/index.html
sudo cp ~/Linux-Repo/LH2.gif /var/www/html/LH2.gif
sudo cp ~/Linux-Repo/app.py ~/lemp-app/app.py
sudo cp ~/Linux-Repo/lemp-app /etc/nginx/sites-available/lemp-app
sudo cp ~/Linux-Repo/lemp-app.service /etc/systemd/system/lemp-app.service

# Startataan service uudelleen
sudo systemctl restart lemp-app
sudo systemctl daemon-reload
