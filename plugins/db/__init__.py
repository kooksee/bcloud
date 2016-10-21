from pony.orm import Database, sql_debug

import config
from plugins.utils import singleton


@singleton
class DB(Database): pass


db = DB('sqlite', config.DBFILE, create_db=True)
sql_debug(True)


if __name__ == '__main__':
    pass
