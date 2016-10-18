# coding:utf-8
# -*- coding:utf-8 -*-

import tornado.gen
import tornado.web
from tornado.escape import json_encode


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('homepage.html')

    @tornado.web.asynchronous
    def post(self):
        name = self.get_secure_cookie('name')
        msg = self.get_argument('msg', '')

        if name == '':
            name = 'Anonymous'

        print name, msg

        data = json_encode({'name': name, 'msg': msg})
        self.write(json_encode({'result': True}))
        self.finish()
