FROM nginx
RUN mkdir -p /srv/static
#RUN chmod 755 /srv/static
COPY ./nginx.conf /etc/nginx/nginx.conf