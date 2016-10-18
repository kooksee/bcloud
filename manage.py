# coding:utf-8
import os

import tornado.web
from tornado.ioloop import IOLoop

import config
from bcloud.handlers.agent import AgentServer
from bcloud.handlers.index import MainHandler
from bcloud.uimodule import EntryModule, SidebarModule
from tornado.options import define, options, parse_command_line

from plugins import db

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="blog", help="blog database name")
define("mysql_user", default="blog", help="blog database user")
define("mysql_password", default="blog", help="blog database password")


class Application(tornado.web.Application):
    def __init__(self):
        self.db = db.DB('sqlite', config.DBFILE, create_db=True)
        self.config = config
        self.agent = AgentServer(application=self)

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={
                "Entry": EntryModule,
                "Sidebar": SidebarModule,
            },
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )

        handlers = [
            (r"/", MainHandler),
            # (r"/websocket", BCloudSocketHandler),
            # (r"/host", HostHandler),
            # (r"/entry/([^/]+)", EntryHandler),
            # (r"/compose", ComposeHandler),
            # (r"/auth/create", AuthCreateHandler),
            # (r"/auth/login", AuthLoginHandler),
            # (r"/auth/logout", AuthLogoutHandler),
        ]

        super(Application, self).__init__(handlers, **settings)


if __name__ == "__main__":
    parse_command_line()

    app = Application()
    app.listen(options.port)
    print "http://{}:{}".format("localhost", options.port)

    # print "listen tcp 8888"
    # app.agent.listen(8888)

    IOLoop.current().start()
