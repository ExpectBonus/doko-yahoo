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
