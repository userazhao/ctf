FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apache2
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN wget https://github.com/userazhao/ctf/raw/main/website.zip -O website.zip
RUN unzip -j website.zip 
RUN mv -v website/* /var/www