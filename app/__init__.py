from flask import Flask
from app.database import db
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_pyfile("config.py")  # It's in my gitignore
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:mypassword@localhost/api_imoveis'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SECRET_KEY = "My secret key that nobody knows"
# JWT_SECRET_KEY = "If I tell you I will have to kill you"
# JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1) timedelta is a function of datetime

db.init_app(app)
ma = Marshmallow(app)
JWTManager(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL,
                                              API_URL,
                                              config={'app_name': "Test application"},
                                              )

app.register_blueprint(swaggerui_blueprint)

from app.authentication import auth
app.register_blueprint(auth)

from app.api_views import api
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)

