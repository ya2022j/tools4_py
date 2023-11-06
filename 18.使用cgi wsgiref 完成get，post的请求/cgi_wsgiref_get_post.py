from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

import os
import sys
import cgi
import json


# cgi wsgiref
# WSGIアプリケーションのリクエスト情報の取得を実装する
# https://qiita.com/sti320a/items/f20b8cbc06bf70425d33


# post ok  /get ok

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    method = environ.get('REQUEST_METHOD')

    content_length = environ.get('CONTENT_LENGTH', 0)

    if method == 'POST':
        body = environ.get('wsgi.input').read(int(content_length))
        print('body: {}'.format(body))
    elif method == 'GET':
        query = environ.get('QUERY_STRING')
        print('query:{}'.format(query))
        return ['Hello, World'.encode('utf-8')]
    return ['Hello, World'.encode('utf-8')]


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
