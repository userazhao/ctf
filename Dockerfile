FROM ubuntu:latest

RUN apt-get apache2

RUN wget https://github.com/userazhao/ctf/archive/main.zip -O ctf.zip

RUN apt-get unzip

RUN unzip ctf.zip -d /var/www