FROM ubuntu:latest

RUN apt update

RUN apt-get install apache2

RUN wget https://github.com/userazhao/ctf/raw/main/website.zip -O ctf.zip

RUN apt-get unzip

RUN unzip ctf.zip -d /var/www