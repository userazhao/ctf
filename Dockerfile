FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apache2
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN wget https://github.com/userazhao/ctf/raw/main/website.zip -O ctf.zip
RUN unzip -j ctf.zip -d /var/www