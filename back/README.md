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

## OAuth2認証に関する情報
doko-yahoo/back/.env ファイル
に秘密情報(現在はGOOGLE_CLIENT_IDのみ)を記載するとFlaskが環境変数として読み込んでくれる

```
GOOGLE_CLIENT_ID="<<OAuth2認証用のグーグルクライアントID>>"
```

.gitignoreによってGitの追跡を防いでいるので、別個に共有する必要がある

### これをやる理由
publicリポジトリに秘密情報を置きたくないため
