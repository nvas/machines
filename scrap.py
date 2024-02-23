from db import DB
from debug import debug
from random import random
# databse name
db = DB("machines.db")

# init connection
db.connect()

enable_keys= """PRAGMA foreign_keys = ON;"""
db.execute_query(enable_keys)


# Create a table machines
create_table_machines_query = """
CREATE TABLE IF NOT EXISTS machines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
"""
db.execute_query(create_table_machines_query)

# Create a table parts
create_table_parts_query = """
CREATE TABLE IF NOT EXISTS parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (machine_id) REFERENCES machines(id)
);
"""
db.execute_query(create_table_parts_query)

# Create a table oil
create_table_oil_query = """
CREATE TABLE IF NOT EXISTS oils (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (machine_id) REFERENCES machines(id)
);
"""

db.execute_query(create_table_oil_query)

# --------------------------------------------------
'''
# Insert some data to table machines
insert_data_to_machines_query = """
INSERT INTO machines (name) VALUES
('machine_name1'),
('machine_name2');
"""
db.execute_query(insert_data_to_machines_query)



# Insert some data to table parts
NUM_MACHINES = 3
NUM_PARTS = 8
NUM_OILS = 8

for m in range(1, NUM_MACHINES):
    for p in range(0, NUM_PARTS):
        insert_data_to_parts_query = f'INSERT INTO parts (machine_id, name) VALUES ({m},\'A{p}\')'
        db.execute_query(insert_data_to_parts_query)

    for o in range(0, NUM_OILS):
        insert_data_to_oils_query = f'INSERT INTO oils (machine_id, name) VALUES ({m},\'A{o}\')'
        db.execute_query(insert_data_to_oils_query)

# Fetch data from table parts
fetch_data_query = "SELECT * FROM parts WHERE machine_id=1"
rows = db.fetch_query(fetch_data_query)
if rows:
    for row in rows:
        print(row)
else:
    print('no records found')

# Fetch data from table oils
fetch_data_query = "SELECT * FROM oils WHERE machine_id=1"
rows = db.fetch_query(fetch_data_query)
if rows:
    for row in rows:
        print(row)
else:
    print('no records found')
'''
# Fetch data from table oils
fetch_data_query = "SELECT * FROM oils"
rows = db.fetch_query(fetch_data_query)
if rows:
    for row in rows:
        print(row)
else:
    print('no records found')


db.disconnect()
