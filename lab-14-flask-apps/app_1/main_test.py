from flask import Flask, render_template
from flask_restplus import Resource, Api # , apidoc

# Import apidoc for monkey patching
from flask_restplus.apidoc import apidoc
from flask_cors import CORS


URL_PREFIX = '/api'

# Make a global change setting the URL prefix for the swaggerui at the module level
# apidoc.url_prefix = URL_PREFIX
# apidoc.spec
# static_url_path=URL_PREFIX,=/
app = Flask(__name__)
# blueprint = Blueprint('api1', 'blueprint_name_1',  url_prefix=URL_PREFIX) #, static_url_path=URL_PREFIX)
# api = Api(blueprint, doc='/doc', title='0- API0 Documentation', version='3.0' ) # prefix='/api0'
# apidoc.specs_url = '/abc'
# app.register_blueprint(blueprint)
CORS(app)


# rewrite template urls to use relative paths to work with reverse proxy
@apidoc.add_app_template_global
def swagger_static(filename):
        return f"./swaggerui/{filename}"

# api = Api(app=app, version="3.0")  # this also works with something like doc="/doc"

api = Api(app=app, version="3.0")  # this also works with something like doc="/doc"
@api.documentation
def custom_ui():
    return render_template(
        "swagger-ui.html", title=api.title, specs_url="./app_2/swagger.json"
    )


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world2'}

if __name__ == '__main__':
    print(__name__)
    app.run(debug=True)
    
    