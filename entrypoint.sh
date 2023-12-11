#!/bin/bash

# Charger le fichier cron
crontab /app/crontab

# Démarrer le service cron en arrière-plan
#service cron start
sleep 5

cron && tail -f /app/cron.log
