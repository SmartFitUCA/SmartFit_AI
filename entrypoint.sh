#!/bin/sh

echo '[INFO] STARTING AI MODEL TRAINING SERVER'
echo '[INFO] LAUNCH CRON IN BACKGROUND'

service cron start
service cron status

python3 /app/testFinal.py

while true; do
  if [ -f "/app/cron_exist.cron" ]; then
    echo "YES CRON WORKS"
    break;
  fi

  echo "[CRON LOGS] "$(grep 'CRON' /var/log/syslog)""
    
  sleep 10
done

sleep infinity
