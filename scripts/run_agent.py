# -*- coding:utf-8 -*-

import socket
import threading

import tornado
from tornado.escape import to_unicode
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.tcpclient import TCPClient

from tornado import iostream


class SimpleTCPClient(object):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._stream = None
        self.EOF = b'\n'

    def _on_write_complete(self):
        print "sent ok"

    def _on_read_line(self, data):
        print data

        self._stream.read_until('\n', self._on_read_line)

    def on_close(self):
        print('exit ...')
        quit()

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self._stream = iostream.IOStream(sock)

        self._stream.connect((self._host, self._port), self.start)

        self._stream.set_close_callback(self.on_close)
        self._stream.read_until('\n', self._on_read_line)

    def start(self):
        t2 = threading.Thread(target=self.send_msg)
        t2.daemon = True
        t2.start()

    def send_msg(self):
        while True:
            data = raw_input("input:")
            a = bytes(data) + self.EOF
            self._stream.write(a)


if __name__ == '__main__':
    try:
        client = SimpleTCPClient('localhost', 8888)
        client.connect()
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        print e
