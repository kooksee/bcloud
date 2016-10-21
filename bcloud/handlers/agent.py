# encoding=utf-8

import socket

from tornado import gen, iostream
from tornado.tcpserver import TCPServer

from plugins.log import logger


class TcpHandler(object):
    def __init__(self, stream, clients, application):
        self.stream = stream

        self.app = application

        self.clients = clients
        self.client_addr = None

        self.stream.socket.setsockopt(
            socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.stream.socket.setsockopt(
            socket.IPPROTO_TCP, socket.SO_KEEPALIVE, 1)
        self.stream.set_close_callback(self.on_disconnect)

    def on_disconnect(self):
        del self.clients[self.client_addr]
        logger.info("删除{}成功".format(self.client_addr))

    @gen.coroutine
    def on_message(self):
        try:
            while True:
                line = yield self.stream.read_until(b'\n')
                text_line = line.decode('utf-8').strip()
                print text_line
                self.stream.write(line)
                print self.clients

        except iostream.StreamClosedError, e:
            print e

    @gen.coroutine
    def connect(self):
        try:
            self.client_addr = '%s:%d' % self.stream.socket.getpeername()
            self.clients[self.client_addr] = self.stream
        except Exception, e:
            print e

        yield self.on_message()


class AgentServer(TCPServer):
    def __init__(self, application=None, io_loop=None, ssl_options=None, **kwargs):
        self.clients = {}  # 保存连接的tcp客户端
        self.application = application
        super(AgentServer, self).__init__(io_loop=io_loop, ssl_options=ssl_options, **kwargs)

    @gen.coroutine
    def handle_stream(self, stream, address):
        yield TcpHandler(stream, self.clients, self.application).connect()
