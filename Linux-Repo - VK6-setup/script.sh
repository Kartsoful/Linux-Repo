#!/bin/bash

# Scriptillä ladataan git repo ja siirretään
# päivitetyt tiedostot niille kuuluville sijainneille
echo "Päivitetään lemp-containers repoa..."
git pull

# siirtää päivitetyt tiedoston oikeisiin paikkoihin

sudo cp ~/Linux-Repo/mysql-deployment.yaml /home/ubuntu/kube/mysql-deployment.yaml
sudo cp ~/Linux-Repo/mysql-pvc.yaml /home/ubuntu/kube/mysql-pvc.yaml
sudo cp ~/Linux-Repo/backend-configmap.yaml /home/ubuntu/kube/backend-configmap.yaml
sudo cp ~/Linux-Repo/backend-deployment.yaml /home/ubuntu/kube/backend-deployment.yaml
sudo cp ~/Linux-Repo/frontend-deployment.yaml /home/ubuntu/kube/frontend-deployment.yaml
sudo cp ~/Linux-Repo/kube_backend/requirements.txt /home/ubuntu/kube/backend/requirements.txt
sudo cp ~/Linux-Repo/kube_backend/Dockerfile /home/ubuntu/kube/backend/Dockerfile
sudo cp ~/Linux-Repo/kube_frontend/nginx.conf /home/ubuntu/kube/frontend/nginx.conf
sudo cp ~/Linux-Repo/kube_frontend/Dockerfile /home/ubuntu/kube/frontend/Dockerfile
sudo cp ~/Linux-Repo/kube_frontend/index.html /home/ubuntu/kube/frontend/index.html
sudo cp ~/Linux-Repo/lemp-app /etc/nginx/sites-available/lemp-app
sudo cp ~/Linux-Repo/index.html /var/www/html/index.html


# Anonymisoidut
# sudo cp ~/Linux-Repo/mysql-secret.yaml /home/ubuntu/kube/mysql-secret.yaml
# sudo cp ~/Linux-Repo/kube_backend/app.py /home/ubuntu/kube/backend/app.py

# Vanhojen tiedostojen porttimuutokset
# sudo cp ~/Linux-Repo/api.py /home/ubuntu/mqtt-chat/api.py
# sudo cp ~/Linux-Repo/lemp-app.service /etc/systemd/system/lemp-app.service

sudo systemctl reload nginx
sudo systemctl daemon-reload
sudo systemctl restart lemp-app
sudo systemctl restart mqtt-api.service

echo "Päivitys valmis!"

