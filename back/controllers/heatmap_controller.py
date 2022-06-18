from flask import request, jsonify
from flask.blueprints import Blueprint
from models.models import *
from db import db

from sqlalchemy import select, func

# heatmapカテゴリのエンドポイント定義
heatmap_blueprint = Blueprint('heatmap', __name__, url_prefix="/api/heatmap")

# ヒートマップの取得
@heatmap_blueprint.route('/<string:job>', methods=['GET'])
def heatmap_handler(job):
    
    hobby_list = request.args.getlist("hobbies")
    num = len(hobby_list)
    
    subquery = ""
    # 趣味リスト指定なし
    if num == 0:
        subquery = db.session.query(User.id)
    # 趣味リスト指定あり
    else:
        subquery = db.session.query(UserHobby.user_id)\
            .join(Hobby, UserHobby.hobby_id==Hobby.id, isouter=False)\
            .filter(Hobby.name.in_(hobby_list))\
            .group_by(UserHobby.user_id)\
            .having(func.count(UserHobby.hobby_id) >= num)

    users = []
    # 職種指定なし
    if job == "all":
        users = User.query.filter(User.id.in_(subquery)).all()
    # 職種指定あり
    elif job == "engineer" or job == "designer" or job == "business":
        users = User.query.filter(User.id.in_(subquery),User.job==job).all()
    else:
        return "Invalid job", 400


    # 集計したユーザの希望都道府県の値を増やしていく
    data = [0 for _ in range(47)]
    for user in users:
        if user.second_pref==None:
            data[user.first_pref-1] += 6
        elif user.third_pref==None:
            data[user.first_pref-1] += 4
            data[user.second_pref-1] += 2
        else:
            data[user.first_pref-1] += 3
            data[user.second_pref-1] += 2
            data[user.third_pref-1] += 1
    
    # 最大値を1に
    data_max = max(data)
    data = list(map(lambda x: float(x)/data_max,data))

    # GetHeatmapResponse
    return jsonify({
        "data": data
    }) 
