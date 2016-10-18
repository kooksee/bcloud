# -*- coding:utf-8 -*-

import os

from os import listdir
from os.path import join as pathjoin, dirname, abspath
import settings

BASEPATH = dirname(__file__)

DBFILE = pathjoin(BASEPATH, "files", "bcloud.db")

if __name__ == '__main__':
    print BASEPATH


def get_settings(name, default=None):
    return settings.__dict__.get(name, default)
