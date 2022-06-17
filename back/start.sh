#!/bin/bash
flask db migrate
flask db upgrade
uwsgi --http 0.0.0.0:5000 --buffer-size=32768 --module app:app
# プロダクションコードではsockerにすべき?-> uwsgi --socket 0.0.0.0:5000 --buffer-size=32768 --module app:app

