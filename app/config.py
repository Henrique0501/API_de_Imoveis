from datetime import timedelta

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:#Henrique0501#@localhost/api_imoveis'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "My secret key that nobody knows"
JWT_SECRET_KEY = "If I tell you I will have to kill you"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
