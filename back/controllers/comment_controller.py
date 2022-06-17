from flask import request, jsonify
from flask.blueprints import Blueprint
from models.models import *
from db import db

# commentカテゴリのエンドポイント定義
comment_blueprint = Blueprint('comments', __name__, url_prefix="/comments")

# GET /comments/{pref_id} と POST /comments/{pref_id}
@comment_blueprint.route('/<int:pref_id>', methods=['GET','POST'])
def comment_handler(pref_id):
    if pref_id < 1 or pref_id > 47:
        return "Invalid prefecture ID", 400

    # 都道府県コメントの取得
    if request.method == 'GET':
        comments = Comment.query\
            .join(User, Comment.user_id==User.id, isouter=False)\
            .with_entities(Comment.comment, User.job, User.born_pref)\
            .filter(Comment.pref==pref_id)\
            .all()
        # GetCommentsResponse
        return jsonify({
            "comments": list(map(
                lambda x: { 
                    "comment": x.comment,
                    "job": x.job,
                    "born_pref": x.born_pref
                    }
                , comments
            ))
        })

    # 都道府県コメントの投稿
    else:
        user = User.query.filter(User.id==request.json["id"]).first()
        if user == None:
            return "Invalid user ID", 400
        
        new_comment = Comment(
            pref=pref_id,
            user_id=request.json["id"],
            comment=request.json["comment"]
        )

        db.session.add(new_comment)
        db.session.commit()
        
        return "Successful operation", 200
        
