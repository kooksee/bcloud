# -*- coding:utf-8 -*-
import tablib
from pony.orm import db_session, commit, select
from tornado import web
from tornado.escape import json_encode

from bcloud.model.host import Host


class HostHandler(web.RequestHandler):
    def get(self):
        with db_session:
            data = tablib.Dataset(
                headers=["name", 'ip', 'id']
            )
            s = select((h.name, h.ip, h.id) for h in Host)[:]
            map(data.append, s)

            print self.application.agent
            print self.application.agent.clients

            self.write(data.json)

    @web.asynchronous
    def post(self):
        with db_session:
            a = Host(name="111", ip="111", port=22, password="111")
            commit()
        print self.request.body
        self.write(json_encode({'result': '测试接口通过'}))
        self.finish()


if __name__ == '__main__':
    with db_session:

        data = tablib.Dataset(
            headers=["name", 'ip', 'id']
        )

        s = select((h.name, h.ip, h.id) for h in Host)[:]
        map(data.append, s)
        print data.json

        for h in select(h for h in Host):
            print h.name
            print h.id
