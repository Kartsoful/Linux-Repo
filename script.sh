#!/bin/bash

# Scriptillä ladataan git repo ja siirretään
# päivitetyt tiedostot niille kuuluville sijainneille

cd /home/ubuntu/Linux-Repo/
git pull

# siirtää päivitetyt tiedoston oikeisiin paikkoihin
# sudo cp ~/Linux-Repo/LH2.gif /var/www/html/LH2.gif
# sudo cp ~/Linux-Repo/lemp-app.service /etc/systemd/system/lemp-app.service
# sudo cp ~/Linux-Repo/streamlit_test.py /home/ubuntu/lemp-app/streamlit_test.py
# sudo cp ~/Linux-Repo/streamlit.service /etc/systemd/system/streamlit.service
# sudo cp ~/Linux-Repo/fetch_weather.sh /home/ubuntu/cron_assignment/fetch_weather.sh
# sudo cp ~/Linux-Repo/fetch_weather.py /home/ubuntu/cron_assignment/fetch_weather.py
# sudo cp ~/Linux-Repo/lemp-app_configure/config.toml /home/ubuntu/lemp-app/.streamlit/config.toml
# sudo cp ~/Linux-Repo/fetch_BTC.py /home/ubuntu/crypto/fetch_BTC.py
# sudo cp ~/Linux-Repo/BTCapp.py /home/ubuntu/crypto/BTCapp.py
# sudo cp ~/Linux-Repo/btc_configure/config.toml /home/ubuntu/crypto/.streamlit/config.toml
# sudo cp ~/Linux-Repo/btc-trend.service /etc/systemd/system/btc-trend.service
sudo cp ~/Linux-Repo/index.html /var/www/html/index.html
sudo cp ~/Linux-Repo/index_chat.html /var/www/html/chat/index_chat.html
sudo cp ~/Linux-Repo/lemp-app /etc/nginx/sites-available/lemp-app
sudo cp ~/Linux-Repo/mosquitto.conf /home/ubuntu/mqtt-chat/mosquitto/config/mosquitto.conf
sudo cp ~/Linux-Repo/docker-compose.yml /home/ubuntu/mqtt-chat/docker-compose.yml
sudo cp ~/Linux-Repo/mqtt-logger.service /etc/systemd/system/mqtt-logger.service

# Anonymisoidut - Jos muokkauksia on tehty, poista kommentointi ja palauta rivit
# sudo cp ~/Linux-Repo/mqtt_logger.py /home/ubuntu/mqtt-chat/mqtt_logger.py

# Startataan service uudelleen
sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl restart lemp-app
sudo systemctl restart streamlit
sudo systemctl restart btc-trend

echo "Päivitys valmis!"

