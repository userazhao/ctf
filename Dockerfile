FROM ubuntu:latest

RUN apt update -y

RUN apt install -y apache2

RUN wget https://github.com/userazhao/ctf/raw/main/website.zip -O ctf.zip

RUN apt install -y unzip

RUN unzip ctf.zip -d /var/www