#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn conf.wsgi:application --log-file -