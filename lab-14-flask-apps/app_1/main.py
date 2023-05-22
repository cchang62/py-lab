# from flask import Flask
# app = Flask(__name__)
# 
# @app.route('/')
# def index():
#     return 'Hello, APP_1'
# 
# if __name__ == '__main__':
#     app.run(port=8081,host='0.0.0.0')


from flask import Flask
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8081)