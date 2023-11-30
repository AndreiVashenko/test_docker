FROM python:alpine3.12

WORKDIR /app

COPY . .

VOLUME myVol1

CMD ["python", "main.py"]
