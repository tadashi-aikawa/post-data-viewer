#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import io
import json

import bottle
from bottle import run, get, request, response, error 

app = bottle.Bottle()

@app.get('/ping')
def ping():
    # if need
    # response.set_header('Access-Control-Allow-Origin', '*')
    return {"success": True}


@app.post('/data')
def print_post_data():
    print(json.dumps(request.json, indent=4, ensure_ascii=False))
    return {"success": True}


@app.error(500)
def error500(error):
    result = {
        "message": "Internal Server Error.",
        "note": "サーバプログラムの管理者に問い合わせて下さい"
    }

    response.content_type = 'application/json; charset=utf-8'
    return json.dumps(result)


@app.error(404)
def error404(error):
    result = {
        "message": "Item not found.",
        "note": "アクセスしているURLが間違っていないことを確認して下さい"
    }

    response.content_type = 'application/json; charset=utf-8'
    return json.dumps(result)


@app.error(405)
def error405(error):
    result = {
        "message": "Method not allowed.",
        "note": "メソッドが正しいことを確認して下さい"
    }

    response.content_type = 'application/json; charset=utf-8'
    return json.dumps(result)


def error400(message, note):
    result = {
        "message": message,
        "note": note
    }

    response.content_type = 'application/json; charset=utf-8'
    response.status = 400
    return json.dumps(result)


run(app, host='0.0.0.0', port=8088, debug=False, reloader=True)