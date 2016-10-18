from pony.orm import Database

import config
from plugins.utils import singleton


@singleton
class DB(Database): pass



if __name__ == '__main__':
    pass
