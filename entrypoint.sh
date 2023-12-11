#!/bin/bash

# Charger le fichier cron
crontab /app/crontab

# Démarrer le service cron en arrière-plan
#service cron start
sleep 5

pip install --no-cache-dir -r requirements.txt 

cron && tail -f /app/cron.log
