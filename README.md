# abstruct
Implemented a combination of nginx, gunicorn, and flask in docker.
Returns the similarity of two sentences using web api from host.

dockerでnginx + gunicorn + flaskを実装しています。
hostからweb apiを呼び出して、2文の類似度を返却します。

## Reference
Refered to the following articles.

下記記事を参考にさせていただきました。

* [Nginx+gunicorn構成でFlaskを使う【ローカル環境編】](https://qiita.com/mintak21/items/eeba4654a0db21abcb1c)
* [[イメージ図付]Nginx+gunicorn+FlaskをDocker化[前編]](https://qiita.com/mintak21/items/d956389ee9338e6c0fe0)
* [[イメージ図付]Nginx+gunicorn+FlaskをDocker化[後編]](https://qiita.com/mintak21/items/00a13e3699588c72b965)

## How to use
The two sentences to be entered are supported only in Japanese.

入力する2文は日本語のみに対応しています。

1. `cd sim_api`
2. `docker-compose -f deployment/docker-compose/docker-compose.yml up` For bagged ground, add the `-d` option
3. `curl "http://localhost:9090/get_sim?sentence1=私はサッカーが好きだ&sentence2=彼は野球が好きだ"`

## FAQ
* When executing the `docker-compose up` command, it stops at the sentence-BERT part.
⇒Remove the image with `docker-compose -f deployment/docker-compose/docker-compose.yml down --rmi all` as it may not work due to cache buildup.
* `docker-compose up`時にsentence-BERTの部分で止まる
⇒キャッシュがたまっていて上手くいかない可能性があるので`docker-compose -f deployment/docker-compose/docker-compose.yml down --rmi all`でイメージを削除する