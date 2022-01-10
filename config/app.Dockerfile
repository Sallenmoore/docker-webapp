FROM python:3.10-alpine


# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

COPY ./gunicorn.py /var/tmp/conf.py
COPY ./entrypoint.sh /var/tmp/entrypoint.sh