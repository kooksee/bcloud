# coding:utf-8
import os

from tornadio2 import TornadioRouter, SocketServer
from tornado import web
from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line

import config
from bcloud.handlers.agent import AgentServer
from bcloud.uimodule import EntryModule, SidebarModule
from plugins.db import db

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="blog", help="blog database name")
define("mysql_user", default="blog", help="blog database user")
define("mysql_password", default="blog", help="blog database password")


class Application(web.Application):
    def __init__(self):
        self.db = db
        self.config = config
        self.agent = AgentServer(application=self)

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={
                "Entry": EntryModule,
                "Sidebar": SidebarModule,
            },
            xsrf_cookies=False,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
            socket_io_port=8888,
        )

        from bcloud.handlers.host import HostHandler
        from bcloud.handlers.index import MainHandler
        from bcloud.handlers.websocket import PingConnection

        PingRouter = TornadioRouter(
            PingConnection,
            dict(
                enabled_protocols=[
                    'websocket',
                    'xhr-polling',
                    'jsonp-polling',
                    'htmlfile'
                ]
            )
        )
        handlers = PingRouter.apply_routes(
            [
                (r"/hh(.*)", MainHandler, dict(database="hello")),
                (r"/host", HostHandler),
                # (r"/websocket", BCloudSocketHandler),
                # (r"/host", HostHandler),
                # (r"/entry/([^/]+)", EntryHandler),
                # (r"/compose", ComposeHandler),
                # (r"/auth/create", AuthCreateHandler),
                # (r"/auth/login", AuthLoginHandler),
                # (r"/auth/logout", AuthLogoutHandler),
            ]
        )

        super(Application, self).__init__(handlers, **settings)


if __name__ == "__main__":
    parse_command_line()

    app = Application()

    print "listen tcp 8887"
    # 要先启动,不然的话得不到客户端链接
    app.agent.listen(8887)

    SocketServer(app)
    print "http://{}:{}".format("localhost", 8888)

    IOLoop.current().start()
