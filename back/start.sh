#!/bin/bash
flask db migrate
flask db upgrade
pytest -v test/user_test.py
pytest -v test/comment_test.py
pytest -v test/heatmap_test.py
uwsgi --http 0.0.0.0:5001 --buffer-size=32768 --module app:app
# プロダクションコードではsocketにすべき?-> uwsgi --socket 0.0.0.0:5001 --buffer-size=32768 --module app:app

