FROM ubuntu:22.10

WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install python3-opencv -y
RUN apt-get install python3-pip -y 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./app.py" ]