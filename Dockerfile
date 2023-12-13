FROM python:3.10
WORKDIR /app
COPY . .
# Cron
RUN apt-get update && apt-get -y install cron
RUN chmod 0644 /app/crontab
RUN crontab /app/crontab
RUN crontab -l
# Python
RUN pip install -r requirements.txt 
ENTRYPOINT ["./entrypoint.sh"]
