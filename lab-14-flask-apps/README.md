# Nginx-Gunicorn-Flask-Docker

## Manual Execution

```sh
cd  LAB-14-FLASK-APPS # <app_root>
gunicorn  -c ./app_1/gunicorn_config.py  main:app --chdir ./app_1
gunicorn  -c ./app_2/gunicorn_config.py  main:app --chdir ./app_2
```

## Docker 

### Build Image

```sh
docker build -t flask-apps -f Dockerfile .
```

### Run Container Locally

```sh
docker run -p 8080:8080 --name flask-apps --rm -d flask-apps

docker log -f flask-apps

docker stop flask-apps
```


