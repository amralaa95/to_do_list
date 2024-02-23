#!/bin/sh

set -x
if [ "$1" = "web" ];
then

    echo "==================="
    echo "Running web app"
    echo "==================="
    echo
    python manage.py migrate
    python manage.py loaddata users_seed.json
    python manage.py collectstatic --no-input
    gunicorn To_Do_List.wsgi --bind 0.0.0.0:8000 --log-level $LOG_LEVEL
fi