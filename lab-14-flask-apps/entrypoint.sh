#!/bin/bash



/opt/venv/bin/gunicorn -c ./app_1/gunicorn_config.py  main:app --chdir ./app_1	# --daemon
# /opt/venv/bin/gunicorn -c ./app_2/gunicorn_config.py  main:app --chdir ./app_2	# --daemon

/opt/venv/bin/gunicorn -c ./app_2/gunicorn_config.py  main_test:app --chdir ./app_2	# --daemon

nginx -g 'daemon off;'