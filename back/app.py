from flask import Flask

from db import init_db

from controllers.user_controller import user_blueprint
from controllers.comment_controller import comment_blueprint
from controllers.heatmap_controller import heatmap_blueprint

import models

from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv(override=True)

app = Flask(__name__)

# アプリ設定の読み込み
app.config.from_object('config.DevelopmentConfig')

# DBの初期化
init_db(app)

# 全エンドポイントをアプリへ登録
app.register_blueprint(user_blueprint)
app.register_blueprint(comment_blueprint)
app.register_blueprint(heatmap_blueprint)

if __name__ == '__main__':
	app.run(host='0.0.0.0')