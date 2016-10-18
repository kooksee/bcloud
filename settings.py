# -*- coding:utf-8 -*-

from sys import modules
from os import listdir
from os.path import abspath, dirname, join as path_join

# Server
DEFAULT_PORT = 8000
DEBUG = True
GZIP = True

# Path
BASE_PATH = dirname(dirname(abspath(__file__)))
STATIC_PATH = path_join(BASE_PATH, "static")
TEMPLATE_PATH = path_join(BASE_PATH, "template")
IGNORE_PATHS = ("library", "mvc", "static", "template", "utest", "doc", "logic")

# Security
COOKIE_SECRET = "32ofdsFDSAfdsaFdsaFDSAfdSAfdSAfDSAfDSAfds65="
COOKIE_USERID = "user"

# Url
LOGIN_URL = "/login"
TEMPLATE_URL = r"/template/(.*)"

# Error
ERROR_404 = "404.html"
