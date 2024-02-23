#!/bin/sh

set -x
if [ "$1" = "web" ];
then

    echo "==================="
    echo "Running Todo list app"
    echo "==================="
    echo
    python manage.py migrate
    python manage.py collectstatic --no-input
    gunicorn To_Do_List.wsgi --bind 0.0.0.0:8000 --log-level $LOG_LEVEL
fi