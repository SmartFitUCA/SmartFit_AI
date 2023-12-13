#!/bin/sh

echo "[INFO] STARTING AI MODEL TRAINING SERVER"
echo "[INFO] LAUNCH CRON IN BACKGROUND"
echo "[INFO] "USER:$USER""

service cron start
service cron status
