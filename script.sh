#!/bin/bash

# Scriptillä ladataan git repo ja siirretään
# päivitetyt tiedostot niille kuuluville sijainneille
echo "Päivitetään lemp-containers repoa..."
git pull

# siirtää päivitetyt tiedoston oikeisiin paikkoihin
# # Tuli tehtyä samalla myös docker-LEMP-kontti
# sudo cp ~/Linux-Repo/docker_backend/requirements.txt /home/ubuntu/lemp-containers/backend/requirements.txt
# sudo cp ~/Linux-Repo/docker_backend/Dockerfile /home/ubuntu/lemp-containers/backend/Dockerfile
# sudo cp ~/Linux-Repo/docker_frontend/index.html /home/ubuntu/lemp-containers/frontend/index.html
# sudo cp ~/Linux-Repo/docker_frontend/nginx.conf /home/ubuntu/lemp-containers/frontend/nginx.conf
# sudo cp ~/Linux-Repo/docker_frontend/Dockerfile /home/ubuntu/lemp-containers/frontend/Dockerfile
# sudo cp ~/Linux-Repo/docker_yml-files/docker-compose.dev.yml /home/ubuntu/lemp-containers/docker-compose.dev.yml
# sudo cp ~/Linux-Repo/docker_yml-files/docker-compose.prod.yml /home/ubuntu/lemp-containers/docker-compose.prod.yml

# Anonymisoidut
# sudo cp ~/Linux-Repo/docker_db/init/init.sql /home/ubuntu/lemp-containers/db/init/init.sql
# sudo cp ~/Linux-Repo/docker_backend/app.py /home/ubuntu/lemp-containers/backend/app.py



# Varsinainen kubernetes
sudo cp ~/Linux-Repo/mysql-deployment.yaml /home/ubuntu/kube/mysql-deployment.yaml
sudo cp ~/Linux-Repo/mysql-pvc.yaml /home/ubuntu/kube/mysql-pvc.yaml
sudo cp ~/Linux-Repo/backend-configmap.yaml /home/ubuntu/kube/backend-configmap.yaml
sudo cp ~/Linux-Repo/backend-deployment.yaml /home/ubuntu/kube/backend-deployment.yaml
sudo cp ~/Linux-Repo/frontend-deployment.yaml /home/ubuntu/kube/frontend-deployment.yaml
sudo cp ~/Linux-Repo/kube_backend/app.py /home/ubuntu/kube/backend/app.py
sudo cp ~/Linux-Repo/kube_backend/requirements.txt /home/ubuntu/kube/backend/requirements.txt
sudo cp ~/Linux-Repo/kube_backend/Dockerfile /home/ubuntu/kube/backend/Dockerfile
sudo cp ~/Linux-Repo/kube_frontend/nginx.conf /home/ubuntu/kube/frontend/nginx.conf
sudo cp ~/Linux-Repo/kube_frontend/Dockerfile /home/ubuntu/kube/frontend/Dockerfile
sudo cp ~/Linux-Repo/kube_frontend/index.html /home/ubuntu/kube/frontend/index.html



# Anonymisoidut
sudo cp ~/Linux-Repo/mysql-secret.yaml /home/ubuntu/kube/mysql-secret.yaml




echo "Päivitys valmis!"

