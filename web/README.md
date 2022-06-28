### 使い方
```
docker-compose build web
docker-compose up -d web
```

### webコンテナの起動に際して注意事項

- 事前にフロントをビルドする
```
docker-compose run front npm run build
```
- OAuth認証情報を作成しておき、クライアントIDをfront/.envとback/.envに記録する
  - 承認済みのJavaScript生成元に念のためhttp://localhost:8000も加える (フロント開発用は8080だが、nginxサーバは8000で動くため)

### URL置き場
https://www.xmisao.com/2014/05/09/nginx-proxy-pass.html