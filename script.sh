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
sudo cp ~/Linux-Repo/streamlit_test.py /home/ubuntu/lemp-app/streamlit_test.py
sudo cp ~/Linux-Repo/Electric_prices.csv /home/ubuntu/lemp-app/Electric_prices.csv
sudo cp ~/Linux-Repo/streamlit.service /etc/systemd/system/streamlit.service
sudo cp ~/Linux-Repo/fetch_weather.sh /home/ubuntu/cron_assignment/fetch_weather.sh

# Startataan service uudelleen
sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl restart lemp-app
sudo systemctl restart streamlit
