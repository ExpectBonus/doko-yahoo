from urllib import response
from flask import Flask, Response, make_response
from flask_jwt_extended import (create_access_token, current_user, jwt_required, set_access_cookies, unset_access_cookies, verify_jwt_in_request)
from flask.blueprints import Blueprint
from models.models import *
from flask import request, jsonify
from flask_jwt_extended import JWTManager
import json

app = Flask(__name__)
jwt = JWTManager(app)
auth_blueprint = Blueprint('login', __name__, url_prefix="/api/auth")

@jwt.user_identity_loader
def identity_user(user):
    return user['id']

@jwt.user_lookup_loader
def lookup_user(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

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
        return jsonify({'msg': 'Wrong login id or password'}), 401

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    app.logger.info('logout started')
    response = make_response()

    unset_access_cookies(response)
    return response, 200

@auth_blueprint.route('/who_am_i', methods=["GET"])
@jwt_required()
def protected():
    result = {
        "id":current_user.id,
        "username":current_user.username,
    }
    resp = make_response(jsonify(result))
    return resp
