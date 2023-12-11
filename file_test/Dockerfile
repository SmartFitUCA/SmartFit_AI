FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY generateurModele.py .

EXPOSE 80

ENTRYPOINT ["python","generateurModele.py"]