FROM python:alpine3.12

WORKDIR /app

COPY . .

#VOLUME C:\temp_os:/temp1

CMD ["python", "main.py"]
