#!/bin/bash

# Charger le fichier cron
crontab /app/crontab

# Démarrer le service cron en arrière-plan
#service cron start

echo "Start"
pip install scikit-learn
cron && tail -f /app/cron.log
echo "End" 
