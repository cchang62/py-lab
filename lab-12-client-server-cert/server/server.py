from flask import Flask
# from flask_sslify import SSLify
from flask import request, redirect
# from OpenSSL import SSL
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.use_privatekey_file('cert/demo-server.key')
# context.use_certificate_file('cert/demo-server.crt') 
context.load_cert_chain('cert/demo-server.crt', 'cert/demo-server.key')

app = Flask(__name__)
# sslify = SSLify(app)

@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # app.run(ssl_context=('cert/demo-server.crt', 'cert/demo-server.key'))
    # app.run(ssl_context=('cert/demo-server.crt', 'cert/demo-server.key'))
    app.run(host='127.0.0.1', debug=False, ssl_context=context)