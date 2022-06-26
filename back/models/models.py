from db import db
from datetime import datetime

PREFECTURES = ["北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県",
"茨城県","栃木県","群馬県","埼玉県","千葉県","東京都","神奈川県",
"新潟県","富山県","石川県","福井県","山梨県","長野県","岐阜県",
"静岡県","愛知県","三重県","滋賀県","京都府","大阪府","兵庫県",
"奈良県","和歌山県","鳥取県","島根県","岡山県","広島県","山口県",
"徳島県","香川県","愛媛県","高知県","福岡県","佐賀県","長崎県",
"熊本県","大分県","宮崎県","鹿児島県","沖縄県"]

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
    password = db.Column(db.String(255), nullable=False)

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