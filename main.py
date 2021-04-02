from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from random import choice, randint

engine = create_engine("sqlite:///college.db", echo=True)
meta = MetaData()

students = Table(
    'students', meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("score", Integer)
)

# create table
# meta.create_all(engine)

# insert data
# with engine.connect() as connection:
#     [
#         connection.execute(students.insert().values(
#             name=f'{choice(["Mike", "Helen", "Steve"])} {randint(0, 10)}'
#         ))
#         for _ in range(20)
#     ]

# select all
with engine.connect() as connection:
    result = connection.execute(students.select())
    rows = result.fetchall()
    print(rows)
