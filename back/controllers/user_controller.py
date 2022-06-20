from flask import request, jsonify
from flask.blueprints import Blueprint
from models.models import *
from db import db

# userカテゴリのエンドポイント定義
user_blueprint = Blueprint('user', __name__, url_prefix="/api/user")

# POST /user/
@user_blueprint.route('/', methods=['POST'])
def post_user_handler():
    user = User.query.filter(User.provider_id==request.json["provider_id"]).first()
    if user == None:
        # ユーザの新規作成
        new_user = User(provider_id=request.json["provider_id"],
                    username=request.json["username"],
                    job=request.json["job"],
                    born_pref=request.json["born_pref"],
                    first_pref=request.json["first_pref"],
                    second_pref=request.json["second_pref"],
                    third_pref=request.json["third_pref"])
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter(User.provider_id==request.json["provider_id"]).first()

        for h in request.json["hobbies"]:
            # 新しい趣味があればhobbiesに追加
            hobby = Hobby.query.filter(Hobby.name==h).first()
            if hobby == None:
                new_hobby = Hobby(name=h)
                db.session.add(new_hobby)
                db.session.commit()
                hobby = Hobby.query.filter(Hobby.name==h).first()
            # ユーザの趣味リスト登録
            new_user_hobby = UserHobby(user_id=user.id,hobby_id=hobby.id)
            db.session.add(new_user_hobby)
            db.session.commit()
        # PostUserResponse
        return jsonify({
            "id": user.id
        })
    else:
        # ユーザの更新
        user.username = request.json["username"]
        user.job = request.json["job"]
        user.born_pref = request.json["born_pref"]
        user.first_pref = request.json["first_pref"]
        user.second_pref = request.json["second_pref"]
        user.third_pref = request.json["third_pref"]
        db.session.add(user)
        db.session.commit()

        # 趣味ではなくなったものを削除
        hobbies = UserHobby.query\
            .join(Hobby, UserHobby.hobby_id==Hobby.id, isouter=False)\
            .with_entities(Hobby.name)\
            .filter(UserHobby.user_id==user.id)\
            .all()        
        for h in list(map(lambda x: x[0],hobbies)):
            hobby = Hobby.query.filter(Hobby.name==h).first()
            now_user_hobby = UserHobby.query.filter(UserHobby.hobby_id==hobby.id,UserHobby.user_id==user.id).first()
            if now_user_hobby not in request.json["hobbies"]:
                db.session.delete(now_user_hobby)
                db.session.commit()

        for h in request.json["hobbies"]:
            # 新しい趣味があればhobbiesに追加
            hobby = Hobby.query.filter(Hobby.name==h).first()
            if hobby == None:
                new_hobby = Hobby(name=h)
                db.session.add(new_hobby)
                db.session.commit()
                hobby = Hobby.query.filter(Hobby.name==h).first()
            # ユーザの趣味リスト登録
            user_hobby = UserHobby.query.filter(UserHobby.hobby_id==hobby.id,UserHobby.user_id==user.id).first()
            if user_hobby==None:
                new_user_hobby = UserHobby(user_id=user.id,hobby_id=hobby.id)
                db.session.add(new_user_hobby)
                db.session.commit()
        # TODO: request.json["hobbies"]にないがそのユーザの趣味として登録されているもの
        #       (かつては趣味だったが今は違うもの)の削除

        # PostUserResponse
        return jsonify({
            "id": user.id
        })

# GET /user/{provider_id} と DELETE /user/{user_id}
@user_blueprint.route('/<string:id>', methods=['GET','DELETE'])
def get_delete_user_handler(id):
    if request.method == "GET":
        provider_id = id
        user = User.query.filter(User.provider_id==provider_id).first()
        if user == None:
            return "user does not exist", 404
        
        hobbies = UserHobby.query\
            .join(Hobby, UserHobby.hobby_id==Hobby.id, isouter=False)\
            .with_entities(Hobby.name)\
            .filter(UserHobby.user_id==user.id)\
            .all()

        # GetUserResponse
        return jsonify({
            "id": user.id,
            "username": user.username,
            "job": user.job,
            "born_pref": user.born_pref,
            "first_pref": user.first_pref,
            "second_pref": user.second_pref,
            "third_pref": user.third_pref,
            "hobbies": list(map(lambda x: x[0],hobbies))
        })
    else:
        user_id = int(id)
        # users, user_hobbies, commentsから該当するユーザのものを削除
        UserHobby.query.filter(UserHobby.user_id==user_id).delete()
        User.query.filter(User.id==user_id).delete()
        Comment.query.filter(Comment.user_id==user_id).delete()
        db.session.commit()
        return "Successfully deleted", 200