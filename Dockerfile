FROM python:alpine3.12

WORKDIR /app

COPY . .

VOLUME C://temp_os:./temp

CMD ["python", "main.py"]
