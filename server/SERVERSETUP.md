Server setup for deployment
===========================
* Start with new DigitalOcean droplet (Ubuntu 14.04)
* Install PostgreSQL(libpq-dev, python-dev, postgresql, postgresql-contrib)
* Install pip3, setup a virtualenv
* From within virtualenv, install django, easy_thumbnails, django-localflavor, psycopg2, gunicorn
* Install nginx
* set up gunicorn config file
* To start gunicorn: /root/svoregistry.com/env/bin/gunicorn -c /root/svoregistry.com/env/gunicorn_config.py svoregistry.wsgi &
* sudo service nginx start
* nginx config: /etc/nginx/sites-available/svoregistry
* symlink /etc/nginx/sites-available/svoregistry to /etc/nginx/sites-enabled/svoregistry
* 