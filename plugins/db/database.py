# -*- coding:utf-8 -*-

from pymongo import *
from pymongo.objectid import ObjectId
from library import *

from config import get_settings


class DB(object):

    DB_SERVER = get_settings("DB_SERVER", "127.0.0.1")
    DB_SERVER_PORT = get_settings("DB_SERVER_PORT", 27017)
    DB_NAME = get_settings("DB_NAME", "blog")

    def __init__(self):
        self._opened = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def open(self):
        if self._opened: return

        self._opened = True
        self._conn = Connection(host = self.DB_SERVER, port = self.DB_SERVER_PORT)
        self._db = self._conn[self.DB_NAME]

    def close(self):
        if not self._opened: return

        self._opened = False
        self._conn.disconnect()

    def __getattr__(self, name):
        return getattr(self._db, name, None)

