from flask import Flask

import pytest 

from db import db
from flask_migrate import Migrate

import models

from controllers.user_controller import user_blueprint
from controllers.comment_controller import comment_blueprint
from controllers.heatmap_controller import heatmap_blueprint


# テスト実行前の共通設定
@pytest.fixture
def app():
    app = Flask(__name__)

    # テスト用コンフィグの読み込み(SQLite使用)
    app.config.from_object('config.TestConfig')

    db.init_app(app)
    Migrate(app,db)
    db.create_all(app=app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(comment_blueprint)
    app.register_blueprint(heatmap_blueprint)

    try:
        yield app
    finally:
        # テスト完了時にテーブルをクリア
        db.drop_all(app=app)