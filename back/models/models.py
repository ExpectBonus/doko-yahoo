from db import db
from datetime import datetime

# ユーザ情報
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    job = db.Column(db.String(255), nullable=False)
    born_pref = db.Column(db.Integer, nullable=False)
    first_pref = db.Column(db.Integer, nullable=False)
    second_pref = db.Column(db.Integer)
    third_pref = db.Column(db.Integer)

# 趣味の一覧
class Hobby(db.Model):

    __tablename__ = 'hobbies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# 各ユーザの趣味
class UserHobby(db.Model):

    __tablename__ = 'user_hobbies'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    hobby_id = db.Column(db.Integer, nullable=False)

# 都道府県へのコメント
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    pref = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255), nullable=False)