#!/bin/bash
flask db migrate
flask db upgrade
uwsgi --http 0.0.0.0:5001 --buffer-size=32768 --module app:app
# プロダクションコードではsocketにすべき?-> uwsgi --socket 0.0.0.0:5001 --buffer-size=32768 --module app:app

