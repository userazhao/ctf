FROM ubuntu:latest

RUN apt-get apache2

RUN cd /var/www

RUN wget 