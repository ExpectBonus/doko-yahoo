from flask import Flask
from flask import request, jsonify

from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)

from flask.blueprints import Blueprint
from models.models import *

import json

app = Flask(__name__)
jwt = JWTManager(app)
auth_blueprint = Blueprint('login', __name__, url_prefix="/api/auth")

# usernameとpasswordでログイン
@auth_blueprint.route('/', methods=['POST'])
def authenticate():
    app.logger.info('login started')

    user = User.query.filter(User.username == request.json["username"], User.password == request.json["password"]).one_or_none()

    if user is not None:
        app.logger.info('login succeeded')
        access_token = create_access_token(identity=json.dumps(user,default=str))
        return jsonify(access_token=access_token), 200
    else:
        app.logger.info('login failed')
        return jsonify({'msg': 'Wrong username or password'}), 401

# JWT検証
@auth_blueprint.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
