import uuid

import datetime
import tornado
from tornadio2 import SocketConnection, event
from tornado.websocket import WebSocketHandler

from plugins.log import logger


class PingConnection(SocketConnection):
    @event
    def ping(self, data):
        now = datetime.datetime.now()
        print data

        return data, [now.hour, now.minute, now.second, now.microsecond / 1000]

    @event
    def stats(self):
        print self.session.server.stats.dump()
        return self.session.server.stats.dump()


class BCloudSocketHandler(WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200

    def get_compression_options(self):
        return {}

    def open(self):
        BCloudSocketHandler.waiters.add(self)

    def on_close(self):
        BCloudSocketHandler.waiters.remove(self)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logger.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logger.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logger.info("got message %r", message)
        parsed = tornado.escape.json_decode(message)
        chat = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
        }
        chat["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=chat))

        BCloudSocketHandler.update_cache(chat)
        BCloudSocketHandler.send_updates(chat)
