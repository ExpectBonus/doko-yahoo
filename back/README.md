# 概要
APIを今回みたいに柔軟に書きたいときはDjangoはかえって面倒っぽいことが判明
(単純なデータの生成・削除・検索機能の自動生成には強いみたい)

そこでFlaskで書いてみたらこっちの方が効率は良かった
Postgreとの接続、6/17現在Swaggerに定義しているAPIの実装は一通りした

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
### ユーザ関連
- ユーザ情報の登録
試しにコマンドラインで
```
curl -X 'POST'   'localhost:5001/user/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "provider_id": "some_id_from_google_or_something",
  "username": "ほげほげ",
  "job": "engineer",
  "born_pref": 46,
  "first_pref": 1,
  "second_pref": 2,
  "third_pref": 5,
  "password": "abc123" <- 追加
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
curl localhost:5001/user/some_id_from_google_or_something
```
を投げればさっき登録したユーザの情報が出るはず
- ユーザ情報の削除
```
curl localhost:5001/user/1
```
でそのIDのユーザが削除できるので、もう一回参照してみると今度は user does not exist と出るはず

### 都道府県別コメント関連
- コメントの投稿
```
curl -X 'POST' \
  'localhost:5001/comments/47' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "comment": "この県こそが至高"
}'
```
- コメントの取得
```
curl localhost:5001/comments/47
```
### ヒートマップ関連
- ヒートマップの取得
```
curl localhost:5001/heatmap/engineer?hobbies=酒好き&hobbies=ゲーマー&hobbies=ピアノ
```

### ログイン
- アクセストークンの取得
- アクセストークンは1時間で期限切れ
```
curl -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d '{"username": "ほげほげ", "password": "abc123"}' localhost:5001/api/auth/
```
```
"access_token": ACCESS_TOKEN
```

- JWTの有効性を検証
```
curl localhost:5001/api/auth/protected -H "Authorization: Bearer ACCESS_TOKEN"
```
```
"logged_in_as": "\"<User id>\""
```

## 実装するうえで参考になる情報
- controllersに各エンドポイントを実装している
  - ユーザ関連はcontrollers/user_controller.py
  - コメント関連はcontrollers/comment_controller.py
  - ヒートマップ関連はcontrollers/heatmap_controller.py
- models/models.pyにデータベースの定義がある
- データベース操作にはSQLAlchemyというライブラリを使っているので
  - SQLAlchemy flask などで調べると機能がいろいろ分かる

## これからやりたいこと
- 即席なのでたぶんバグはある
  - いろんなケースを自分たちで試しつつ、自動テストを書きたい
- 開発と本番で設定を分ける記述が欲しい
- 動作の最適化
  - ヒートマップの取得はforループを使わざるを得なかったりしているので、もっと速いに越したことはない
- (余裕があれば)あったらフロント的に便利そうなAPIを生やす
