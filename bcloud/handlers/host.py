# coding:utf-8
# -*- coding:utf-8 -*-

import tornado


class HostHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie('name', '')
        self.render('index.html')

    @tornado.web.asynchronous
    def post(self):
        name = self.get_secure_cookie('name')
        msg = self.get_argument('msg', '')

        if name == '':
            name = 'Anonymous'

        print name, msg

        data = json_encode({'name': name, 'msg': msg})
        c.publish('test_channel', data)
        self.write(json_encode({'result': True}))
        self.finish()
