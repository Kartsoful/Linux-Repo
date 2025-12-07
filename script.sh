#!/bin/bash

# Scriptillä ladataan git repo ja siirretään
# päivitetyt tiedostot niille kuuluville sijainneille

cd /home/ubuntu/Linux-Repo/
git pull

# siirtää päivitetyt tiedoston oikeisiin paikkoihin
sudo cp ~/Linux-Repo/backend/app.py /home/ubuntu/lemp-containers/backend/app.py
sudo cp ~/Linux-Repo/backend/requirements.txt /home/ubuntu/lemp-containers/backend/requirements.txt
sudo cp ~/Linux-Repo/backend/Dockerfile /home/ubuntu/lemp-containers/backend/Dockerfile
sudo cp ~/Linux-Repo/frontend/index.html /home/ubuntu/lemp-containers/frontend/index.html
sudo cp ~/Linux-Repo/frontend/nginx.conf /home/ubuntu/lemp-containers/frontend/nginx.conf
sudo cp ~/Linux-Repo/frontend/Dockerfile /home/ubuntu/lemp-containers/frontend/Dockerfile
sudo cp ~/Linux-Repo/db/init/init.sql /home/ubuntu/lemp-containers/db/init/init.sql

# sudo cp ~/Linux-Repo/lemp-app.service /etc/systemd/system/lemp-app.service
# sudo cp ~/Linux-Repo/index.html /var/www/html/index.html
# sudo cp ~/Linux-Repo/index_chat.html /var/www/html/chat/index_chat.html
# sudo cp ~/Linux-Repo/lemp-app /etc/nginx/sites-available/lemp-app
# sudo cp ~/Linux-Repo/mosquitto.conf /home/ubuntu/mqtt-chat/mosquitto/config/mosquitto.conf
# sudo cp ~/Linux-Repo/docker-compose.yml /home/ubuntu/mqtt-chat/docker-compose.yml
# sudo cp ~/Linux-Repo/mqtt-logger.service /etc/systemd/system/mqtt-logger.service
# sudo cp ~/Linux-Repo/mqtt_logger.sh /home/ubuntu/mqtt-chat/mqtt_logger.sh
# sudo cp ~/Linux-Repo/api.sh /home/ubuntu/mqtt-chat/api.sh
# sudo cp ~/Linux-Repo/mqtt-api.service /etc/systemd/system/mqtt-api.service


# Startataan service uudelleen
sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl restart lemp-app
sudo systemctl restart streamlit
sudo systemctl restart btc-trend

echo "Päivitys valmis!"

