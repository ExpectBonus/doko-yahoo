from flask import request, jsonify
from flask.blueprints import Blueprint
from models.models import *
from db import db

# heatmapカテゴリのエンドポイント定義
heatmap_blueprint = Blueprint('heatmap', __name__, url_prefix="/heatmap")

@heatmap_blueprint.route('/', methods=['GET'])
def hello_heatmap():
    return "hello, heatmap!"
