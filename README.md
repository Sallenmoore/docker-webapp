# Python Environment

Python based Webapp

## Dev Command Cheatsheet

* docker run -it --name course_app . /bin/bash
* docker-compose pull
* docker-compose up --build -d
* docker-compose down --remove-orphans

* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser --noinput
* python manage.py flush --no-input
* python manage.py collectstatic  --clear
