# -*- coding:utf-8 -*-

from os import listdir
from os.path import exists as path_exists, join as path_join, abspath, isdir, basename


class singleton(object):
    """
        decorator: design patter - singleton
    """

    def __init__(self, cls):
        self.cls = cls
        self.inst = None

    def __call__(self, *args, **kwargs):
        if not self.inst: self.inst = self.cls(*args, **kwargs)
        return self.inst

    def __getattr__(self, name):
        return getattr(self.inst, name)


def read_all_text(path):
    """
        read all text from the file

        return: text or None
    """
    if not path_exists(path): return None
    with open(path, "r") as file: return file.read()


def subdirs(path):
    """
        get all the sub-directories

        return: [(basename, fullname), ...]
    """
    path = abspath(path)
    return filter(
        lambda (b, p): isdir(p),
        [(p, path_join(path, p)) for p in listdir(path) if "." not in p])
