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

# Create a table oils
create_table_oils_query = """
CREATE TABLE IF NOT EXISTS oils (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (machine_id) REFERENCES machines(id)
);
"""
db.execute_query(create_table_machines_query)
db.execute_query(create_table_parts_query)
db.execute_query(create_table_oils_query)


db.disconnect()
