#!/bin/sh

echo "[INFO] STARTING AI MODEL TRAINING SERVER"
echo "[INFO] LAUNCH CRON IN BACKGROUND"

service cron start
service cron status

sleep infinity
