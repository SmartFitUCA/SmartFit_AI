FROM python:3.10
EXPOSE 80
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY generateurModele.py .
COPY testFinal.py .
COPY crontab .

RUN touch /app/cron.log

RUN chmod 0644 /app/crontab
RUN apt-get update
RUN apt-get -y install cron

CMD cron && tail -f /app/cron.log