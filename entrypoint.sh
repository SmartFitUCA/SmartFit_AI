#!/bin/bash

# Charger le fichier cron
crontab /app/crontab

# Démarrer le service cron en arrière-plan
#service cron start

echo "Start"
cron && tail -f /app/cron.log
echo "End" 
