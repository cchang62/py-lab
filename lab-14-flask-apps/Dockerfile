# python 3.6
FROM python:3.6-slim

# install nginx
RUN apt-get update && apt-get install nginx -y
# copy our nginx configuration to overwrite nginx defaults
COPY ./nginx/flask_apps.conf /etc/nginx/conf.d/default.conf
# link nginx logs to container stdout
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

# ENV REQUESTS_CA_BUNDLE="/YYY/xxx.pem"

# copy the django code
COPY . ./app

# change our working directory to the django projcet roo
WORKDIR /app

# create virtual env (notice the location?)
# update pip
# install requirements
RUN python -m venv /opt/venv && \
    /opt/venv/bin/python -m pip install pip --upgrade && \
    /opt/venv/bin/python -m pip install -r requirements.txt

EXPOSE 8080/tcp

# make our entrypoint.sh executable
RUN chmod +x ./entrypoint.sh

# execute our entrypoint.sh file
CMD ["./entrypoint.sh"]
