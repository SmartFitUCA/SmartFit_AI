#!/bin/sh

echo '[INFO] STARTING AI MODEL TRAINING SERVER'
echo '[INFO] LAUNCH CRON IN BACKGROUND'

service cron start
service cron status

while true; do
  if [ -f "/app/cron_exist.cron" ]; then
    echo "YES CRON WORKS"
    break;
  fi

  echo "CRON LOGS"
  cat /app/cron_py.log
     
  sleep 10
done

sleep infinity
