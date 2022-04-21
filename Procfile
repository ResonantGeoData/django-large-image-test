release: ./manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT imaging.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery --app imaging.celery worker --loglevel INFO --without-heartbeat
