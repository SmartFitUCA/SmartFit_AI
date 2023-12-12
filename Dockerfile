FROM python:3.10

EXPOSE 80

WORKDIR /app

# Copier les fichiers nécessaires dans l'image
COPY requirements.txt .
COPY generateurModele.py .
COPY testFinal.py .
COPY crontab .

# Installer les dépendances
#RUN pip install --no-cache-dir -r requirements.txt 

# Créer le fichier de log
RUN touch /app/cron.log

# Donner les permissions nécessaires
RUN chmod 777 /app/crontab

# Installer le service cron
RUN apt-get update && apt-get -y install cron

# Copier le script d'entrée
#COPY entrypoint.sh /app/entrypoint.sh
#RUN chmod +x /app/entrypoint.sh

RUN crontab /app/crontab
RUN crontab -l

# Définir le point d'entrée de l'image
#ENTRYPOINT ["crone"]
