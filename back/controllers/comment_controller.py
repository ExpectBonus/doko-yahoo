from flask import request, jsonify
from flask.blueprints import Blueprint
from models.models import *
from db import db

# commentカテゴリのエンドポイント定義
comment_blueprint = Blueprint('comments', __name__, url_prefix="/comments")

@comment_blueprint.route('/', methods=['POST'])
def hello_comment():
    return "hello, comments!"
