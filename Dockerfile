FROM ubuntu:latest

RUN apt-get apache2

RUN wget https://github.com/userazhao/ctf/raw/main/website.zip -O ctf.zip

RUN apt-get unzip

RUN unzip ctf.zip -d /var/www