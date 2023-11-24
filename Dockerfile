FROM python:alpine3.12

WORKDIR /app

COPY . .

#VOLUME C://temp_os:/temp

VOLUME C:\temp_os\os.txt:/temp

CMD ["python", "main.py"]
