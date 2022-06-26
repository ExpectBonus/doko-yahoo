from flask import Flask
from flask_jwt_extended import JWTManager

from datetime import timedelta

from db import init_db

from controllers.user_controller import user_blueprint
from controllers.comment_controller import comment_blueprint
from controllers.heatmap_controller import heatmap_blueprint
from controllers.login_controller import auth_blueprint

import models

app = Flask(__name__)
jwt = JWTManager(app)

app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

# アプリ設定の読み込み
app.config.from_object('config.DevelopmentConfig')

# DBの初期化
init_db(app)

# 全エンドポイントをアプリへ登録
app.register_blueprint(user_blueprint)
app.register_blueprint(comment_blueprint)
app.register_blueprint(heatmap_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
	app.run(host='0.0.0.0')