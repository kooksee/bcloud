# -*- coding:utf-8 -*-

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

# 访问签名的有效时间, 秒
SIGNATURE_EXPIRE_SECONDS = 3600

HOST = '127.0.0.1'
PORT = 6500

# 是否调试模式
DEBUG = False

# Redis 配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 'your_password'

# MongoDB 配置
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_USERNAME = 'api_gateway_user'
MONGO_PASSWORD = 'api_gateway_password'
MONGO_DBNAME = 'api_gateway'
