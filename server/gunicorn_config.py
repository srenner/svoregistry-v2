command = '/root/svoregistry.com/env/bin/gunicorn'
pythonpath = '/root/svoregistry.com/env/bin'
bind = '127.0.0.1:8001'
workers = 3
errorlog = '/var/log/gunicorn/error.log'
accesslog = '/var/log/gunicorn/access.log'
