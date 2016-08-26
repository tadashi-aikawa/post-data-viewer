# post-data-viewer

postデータを表示するViewer。
webフックの動作確認などに使用して下さい。

## 環境

* Python2.7以上
* Python3.3以上
* 仮想環境が作成できること

## 動作の準備

Linuxの場合

### 初回準備

```
$ git clone https://github.com/tadashi-aikawa/post-data-viewer.git
$ cd post-data-viewer
$ pyvenv venv (or virtualenv venv)
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### 実行

```
$ source venv/bin/activate
$ python src/main.py
```

## 動作確認

`http://${your ip address}:8088/ping` にアクセス。  
エラーにならなければOK。

## 実際の使い方

以下にPOST

* URL
    * `http://${your ip address}:8088/data`
* content-type
    * application/json
* 形式
    * raw
