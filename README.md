# post-data-viewer

postデータを表示するViewer。
webフックの動作確認などに使用して下さい。

## 環境

以下のいずれか

* Dockerが使えること
* Python2.7以上 かつ 仮想環境が作成できること
* Python3.3以上 かつ 仮想環境が作成できること 

## リポジトリ取得

```
$ git clone https://github.com/tadashi-aikawa/post-data-viewer.git
$ cd post-data-viewer
```

## ビルド+実行 (Dockerを使う場合)

```
$ sudo docker build -t post-data-viewer .
$ sudo docker run -it --rm -p 8088:8088 post-data-viewer
```

## ビルド+実行 (Dockerを使わない場合)

```
$ pyvenv venv (or virtualenv venv)
$ source venv/bin/activate
$ pip install -r requirements.txt
$ source venv/bin/activate
$ python src/main.py
```

## 動作確認

`http://${your ip address}:8088` にアクセス。  
エラーにならなければOK。

## 実際の使い方

以下にPOST

* URL
    * `http://${your ip address}:8088/data`
* content-type
    * application/json
* 形式
    * raw
