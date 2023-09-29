from sqlalchemy import create_engine, MetaData, text
from sqlalchemy import Table, Column, Integer, String
from IPython import embed


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata_obj = MetaData()

# create a sqlalchemy table with id, name, age, gender
people_table = Table(
    "people",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
    Column("gender", String),
)

friends_table = Table(
    "friends",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("friend_id", Integer),
)

metadata_obj.create_all(engine)

people_seed_data = [
    {"name": "Alice", "age": 42, "gender": "F"},
    {"name": "Bob", "age": 27, "gender": "M"},
    {"name": "Charlie", "age": 35, "gender": "M"},
    {"name": "David", "age": 19, "gender": "M"},
    {"name": "Emily", "age": 53, "gender": "F"},
    {"name": "Frank", "age": 47, "gender": "M"},
    {"name": "Grace", "age": 31, "gender": "F"},
    {"name": "Henry", "age": 24, "gender": "M"},
    {"name": "Isabel", "age": 39, "gender": "F"},
    {"name": "Jack", "age": 58, "gender": "M"},
]

# iterate over the seed data and insert into the table
with engine.begin() as connection:
    for person in people_seed_data:
        query = people_table.insert().values(**person)
        connection.execute(query)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM people limit 1"))
    for row in result:
        print(f"name:{row.name}")
        embed()
