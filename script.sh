#!/bin/bash

# Scriptillä ladataan git repo ja siirretään
# päivitetyt tiedostot niille kuuluville sijainneille
echo "Päivitetään lemp-containers repoa..."
git pull

# siirtää päivitetyt tiedoston oikeisiin paikkoihin
sudo cp ~/Linux-Repo/backend/requirements.txt /home/ubuntu/lemp-containers/backend/requirements.txt
sudo cp ~/Linux-Repo/backend/Dockerfile /home/ubuntu/lemp-containers/backend/Dockerfile
sudo cp ~/Linux-Repo/frontend/index.html /home/ubuntu/lemp-containers/frontend/index.html
sudo cp ~/Linux-Repo/frontend/nginx.conf /home/ubuntu/lemp-containers/frontend/nginx.conf
sudo cp ~/Linux-Repo/frontend/Dockerfile /home/ubuntu/lemp-containers/frontend/Dockerfile
sudo cp ~/Linux-Repo/docker-compose.dev.yml /home/ubuntu/lemp-containers/docker-compose.dev.yml
sudo cp ~/Linux-Repo/docker-compose.prod.yml /home/ubuntu/lemp-containers/docker-compose.prod.yml

# Anonymisoidut
# sudo cp ~/Linux-Repo/db/init/init.sql /home/ubuntu/lemp-containers/db/init/init.sql
# sudo cp ~/Linux-Repo/backend/app.py /home/ubuntu/lemp-containers/backend/app.py


echo "Päivitys valmis!"

