from tinydb import TinyDB, Query
from Database import Database

class TinyDB(Database):
    def __init__(self, db_file_path):
        self.db = TinyDB(db_file_path)
    
    def create_table(self, table_name):
        # In TinyDB, tables are created implicitly when data is inserted.
        pass
    
    def insert(self, table_name, data):  # Convert ObjectId to string
        table = self.db.table(table_name)
        table.insert(data)
    
    def update(self, table_name, query, data):
        table = self.db.table(table_name)
        table.update(data, Query().search(query))
    
    def delete(self, table_name, query):
        table = self.db.table(table_name)
        table.remove(Query().search(query))
    
    def query(self, table_name, query):
        table = self.db.table(table_name)
        return table.search(Query().search(query))