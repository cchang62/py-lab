from flask import Flask, render_template, Blueprint
from flask_restplus import Resource, Api # , apidoc

# Import apidoc for monkey patching
from flask_restplus.apidoc import apidoc
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# rewrite template urls to use relative paths to work with reverse proxy
@apidoc.add_app_template_global
def swagger_static(filename):
        return f"/swaggerui/{filename}"

# api = Api(app=app, version="3.0")  # this also works with something like doc="/doc"

blueprint = Blueprint('api', __name__, url_prefix='/app_2') # this also works with something like doc="/doc"
api = Api(blueprint, doc='/doc', title='app_2 doc', version="3.5")  
app.register_blueprint(blueprint)

@api.documentation
def custom_ui():
    return render_template(
        "swagger-ui.html", title=api.title, specs_url="./swagger.json"
    )


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': api.base_path}

if __name__ == '__main__':
    print(__name__)
    app.run(debug=True)
    
    