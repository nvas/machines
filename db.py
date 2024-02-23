import sqlite3



# connect(self)
# disconnect(self)
# execute_query(self, query)
# fetch_query(self, query)

class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(f'{self.db_name}')
            self.cursor = self.connection.cursor()
            print("Connected to database:", self.db_name)
        except Exception as e:
            print("Error connecting to database:", e)
            return False


    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from database:", self.db_name)
        else:
            print("Not connected to any database.")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully:", query)
        except Exception as e:
            print("Error executing query:", e)
            return False

    def fetch_query(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print("Error fetching query result:", e)
            return False


    def insert_many(self, query, list_records):
        try:
            self.cursor.executemany(f'{query}', list_records)
            self.cursor.connection.commit()  # Commit changes to the database
            return True
        except Exception as e:
            print(f'Error inserting records: {str(e)}')
            return False


