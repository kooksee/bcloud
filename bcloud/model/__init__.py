# import uuid
#
# from pony.orm import Required, Optional, PrimaryKey, composite_key, composite_index, datetime, Set, sql_debug, Json, \
#     Decimal
#
# from plugins.db import db
#
#
# class MyEntity(db.Entity):
#     attr1 = Required(str)
#     name = Required(str)
#     picture = Optional(buffer)
#
#     name = Required(str, unique=True)
#     price = Required(Decimal)
#     description = Optional(str)
#
#     id = PrimaryKey(int, auto=True)
#     name = Required(str, unique=True)
#     price = Required(Decimal)
#     description = Optional(str)
#
#     email = PrimaryKey(str)
#     name = Required(str)
#
#     a = Required(int)
#     b = Required(str)
#     PrimaryKey(a, b)
#
#     a = Required(str)
#     b = Optional(int)
#     composite_key(a, b)
#
#     a = Required(str)
#     b = Optional(int)
#     composite_index(a, b)
#
#     price = Required(Decimal, 10, 2)  # DECIMAL(10, 2)
#
#     dt = Required(datetime, 6)
#
#     code = Required(uuid.UUID, default=uuid.uuid4)
#
#     created_at = Required(datetime, sql_default='CURRENT_TIMESTAMP')
#     closed = Required(bool, default=True, sql_default='1')
#
#     name = Required(str)
#     gpa = Required(float, py_check=lambda val: val >= 0 and val <= 5)
#
#     _table_ = "person_table"
#     name = Required(str, column="person_name")
#
#
# class Course(db.Entity):
#     name = Required(str)
#     semester = Required(int)
#     lectures = Set("Lecture")
#     PrimaryKey(name, semester)
#
#
# class Lecture(db.Entity):
#     date = Required(datetime)
#     course = Required(Course, columns=["name_of_course", "semester"])
#
#
# sql_debug(True)
# db.generate_mapping(create_tables=True)
#
#
# class Product(db.Entity):
#     id = PrimaryKey(int, auto=True)
#     name = Required(str)
#     info = Required(Json)
#     tags = Optional(Json)
#
#
# db.bind('sqlite', ':memory:', create_db=True)
# db.generate_mapping(create_tables=True)
#
# p1 = Product(name='Samsung Galaxy S7 edge',
#              info={
#                  'display': {
#                      'size': 5.5,
#                  },
#                  'battery': 3600,
#                  '3.5mm jack': True,
#                  'SD card slot': True,
#                  'colors': ['Black', 'Grey', 'Gold'],
#              },
#              tags=['Smartphone', 'Samsung'])
#
# p2 = Product(name='iPhone 6s',
#              info={
#                  'display': {
#                      'size': 4.7,
#                      'resolution': [750, 1334],
#                      'multi-touch': True
#                  },
#                  'battery': 1810,
#                  '3.5mm jack': True,
#                  'colors': ['Silver', 'Gold', 'Space Gray', 'Rose Gold']
#              },
#              tags=['Smartphone', 'Apple', 'Retina'])
