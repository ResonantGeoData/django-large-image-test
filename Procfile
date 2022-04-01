release: ./manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT django_large_image_test.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery --app django_large_image_test.celery worker --loglevel INFO --without-heartbeat
