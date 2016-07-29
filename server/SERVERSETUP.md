Server setup for deployment
===========================
* Start with new DigitalOcean droplet (Ubuntu 14.04)
* Install PostgreSQL(libpq-dev, python-dev(maybe?), python3-dev, postgresql, postgresql-contrib)
  * Setup
    * sudo -u postgres psql;
    * alter user postgres password 'mypassword';
    * create user myusername createdb createuser password 'mypassword';
    * create database mydatabase owner myusername;
    * \q
* Install pip3, setup a virtualenv
  * sudo apt-get install python3-pip #for most modern ubuntu derivatives
  * sudo pip3 install virtualenv
  * virtualenv -p python3 svo #puts a python in a directory called svo
  * source /path/to/activate #new python is now active
* Install python packages from pip
  * django
  * whoosh
  * django-haystack
  * easy_thumbnails
  * django-localflavor
  * psycopg2
  * gunicorn
* Install nginx, configure files in /etc/nginx
* set up gunicorn config file
* To start gunicorn: "/root/svoregistry.com/env/bin/gunicorn -c /root/svoregistry.com/env/gunicorn_config.py svoregistry.wsgi &" from same directory as manage.py
* sudo service nginx start
* nginx config: /etc/nginx/sites-available/svoregistry
* symlink /etc/nginx/sites-available/svoregistry to /etc/nginx/sites-enabled/svoregistry
* Manually backup database
  * pg_dump --username myusername --dbname mydbname > mydbname_mydatestamp.psql
