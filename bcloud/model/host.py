# -*- coding:utf-8 -*-
import uuid

from pony.orm import Required, PrimaryKey

from plugins.db import db


class Host(db.Entity):
    _table_ = 'Host'

    id = PrimaryKey(str, default=str(uuid.uuid4()))
    name = Required(str)
    ip = Required(str)
    port = Required(int)
    password = Required(str)


db.generate_mapping(create_tables=True)

# with db_session:
#     Host(id=str(uuid.uuid4()), name="111", ip="111", port=22, password="111")
#     Host(id=str(uuid.uuid4()), name="222", ip="222", port=22, password="222")
#     commit()
