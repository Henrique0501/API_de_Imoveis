from flask import jsonify, request, make_response, Blueprint
from app.database import db
from app.user_model import User, UserSchema
import datetime
from flask_jwt_extended import create_access_token

auth = Blueprint("authentication", __name__, url_prefix="/auth")


@auth.route('/register', methods=['POST'])
def register():
    us = UserSchema()
    body = request.json

    list_users = [user.username for user in User.query.all()]
    list_ids = [user.id for user in User.query.all()]

    if body['username'] in list_users:
        resp = make_response(jsonify({'message': 'Esse username já está sendo usado'}), 422)
        return resp

    if 'id' in body and body['id'] in list_ids:
        resp = make_response(jsonify({'message': f"O id {body['id']} já está sendo usado. "
                                                 f"Para evitar esse erro, você pode enviar o body sem um id."}), 422)
        return resp

    obj = us.load(body)  # load converts the body (dict) for an object in python (instance od User class)
    db.session.add(obj)
    db.session.commit()

    result = User.query.filter_by(username=body['username']).first()
    result_json = us.dump(result)  # "dumps" converts the var result (that is an instance of User class) to a json
    del result_json['password']
    return result_json


@auth.route('/login', methods=['POST'])
def login():
    body = request.json
    username = body['username']
    password = body['password']

    user = User.query.filter_by(username=username).first()

    if not user:
        return make_response(jsonify({'error': 'non-existent user'}), 404)

    if not user.verify_password(password):
        resp = make_response(jsonify({"error": "Invalid password"}), 403)
        return resp

    payload = {
        "id": user.id,
        "username": user.username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }

    token = create_access_token({"id": user.id})
    return make_response(jsonify({"token": token}), 201)
