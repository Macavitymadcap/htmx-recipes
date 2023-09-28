import sqlite3
from contextlib import closing

class DbContext:
    
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def create_connection(self) -> sqlite3.Connection:
            try:
                connection = sqlite3.connect(self.db_path)
                return connection
            except sqlite3.Error as error:
                raise error
    
    def initialise_db(self, schema_path: str) -> None:
        with closing(self.create_connection()) as connection:
             with open(schema_path) as schema:
                connection.executescript(schema.read())

    