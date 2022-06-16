# 概要
APIを今回みたいに柔軟に書きたいときはDjangoはかえって面倒っぽいことが判明
(単純なデータの生成・削除・検索機能の自動生成には強いみたい)

そこでFlaskで書いてみたらこっちの方が効率は良かった
Postgreとの接続もできている

## 使い方
### 起動方法
doko-yahooフォルダ上で
```
docker-compose build back
docker-compose up -d back
```
再起動もこれを打つだけ
### ログ確認
```
docker ps -a
```
でdokoyahoo_back_1のCONTAINER_IDを確認して
```
docker logs CONTAINER_ID
```

## 今のところ実装してる機能
- データベーススキーマはできた
- ユーザ情報の登録
試しにコマンドラインで
```
curl -X 'POST'   'localhost:5000/user/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "provider_id": "some_id_from_google_or_something",
  "username": "ほげほげ",
  "job": "engineer",
  "born_pref": 46,
  "first_pref": 1,
  "second_pref": 2,
  "third_pref": 5,
  "hobbies": [
    "酒好き",
    "ゲーマー",
    "ピアノ"
  ]
}'
```
を投げてみると {"id": 1} みたいなユーザIDが返ってくるはず
- ユーザ情報の参照
```
curl localhost:5000/user/some_id_from_google_or_something
```
を投げればさっき登録したユーザの情報が出るはず
- ユーザ情報の削除
```
curl localhost:5000/user/1
```
でそのIDのユーザが削除できるので、もう一回参照してみると今度は user does not exist と出るはず

## まだ実装していない機能
- ヒートマップの取得
- 都道府県別コメント

これらをそれぞれ 

- controllers/heatmap_controller.py 
- controllers/comment_controller.py

に実装したい

ユーザ関連の機能はcontrollers/user_controller.py に実装しているので、それが参考になる

加えてmodels/models.pyにデータベースの定義があるので、DB操作時にはそれも参考になる

## 参考情報
- ユーザ関連の機能の実装はcontrollers/user_controller.py にある
- models/models.pyにデータベースの定義がある
- データベース操作にはSQLAlchemyというライブラリを使っているので
  - SQLAlchemy flask などで調べると機能がいろいろ分かる
