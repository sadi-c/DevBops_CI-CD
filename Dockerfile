FROM debian:latest

MAINTAINER Sumaiyah and Dolma

RUN apt-get update && apt-get install -y apache2 \
   libapache2-mod-wsgi-py3 \
   build-essential \
   python3 \
   python3-dev\
   python3-pip \
&& apt-get clean \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /var/www/devbops_blog_microservice/requirements.txt
RUN pip3 install -r /var/www/devbops_blog_microservice/requirements.txt

# Apache config file
COPY ./blog.conf /etc/apache2/sites-available/blog.conf
RUN a2ensite blog
RUN a2enmod headers

# wsgi config file Mod_wsgi
COPY ./blog.wsgi /var/www/devbops_blog_microservice/blog.wsgi

####################
COPY ./devbops_blog_microservice /var/www/devbops_blog_microservice/devbops_blog_microservice

RUN a2dissite 000-default.conf
RUN a2ensite blog.conf

#### LINK LOGS
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
   ln -sf /proc/self/fd/1 /var/log/apache2/error.log

EXPOSE 80
WORKDIR /var/www/devbops_blog_microservice

CMD  /usr/sbin/apache2ctl -D FOREGROUND