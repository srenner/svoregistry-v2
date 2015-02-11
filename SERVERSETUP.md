Server setup for deployment
===========================

* Start with new DigitalOcean droplet (Ubuntu 14.04)
* sudo apt-get update
* sudo apt-get upgrade
* apt-get install python3-pip
* pip3 install virtualenv
* mkdir svoregistry.com
* cd svoregistry.com
* virtualenv env
* source env/bin/activate
* pip3 install django
* mkdir site (project files will eventually go here)
* deactivate (we don't need virtalenv for a while)
* sudo apt-get install libpq-dev python-dev
* sudo apt-get install postgresql postgresql-contrib
* sudo apt-get install nginx
* source env/bin/activate
* sudo su - postgres
* createdb svoregistry
* psql
* create user svo with password '***';
* grant all privileges to database svoregistry to svo;
* \q
* exit
* pip3 install psycopg2
* sudo su - postgres
* ...
* pip3 install easy_thumbnails
* pip3 install django-localflavor
* set up gunicorn
* set up gunicorn config file
* /root/svoregistry.com/env/bin/gunicorn -c /root/svoregistry.com/env/gunicorn_config.py svoregistry.wsgi
* sudo service nginx start
* 
