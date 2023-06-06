from tinydb import TinyDB, Query
from Database import Database


class Local(Database):
    def __init__(self, db_file_path):
        self.db = TinyDB(db_file_path)
        

    def create_table(self, table_name):
        # In TinyDB, tables are created implicitly when data is inserted.
        pass

    def insert(self, table_name, data):  
        table = self.db.table(table_name)
        table.insert(data)

    def update(self, table_name, query, data):
        table = self.db.table(table_name)
        matches = table.search(query)
        for match in matches:
            table.update(data, doc_ids=[match.doc_id])

    def delete(self, table_name, query):
        table = self.db.table(table_name)
        matches = table.search(query)
        for match in matches:
            table.remove(doc_ids=[match.doc_id])

    def query(self, table_name, query):
        table = self.db.table(table_name)
        return table.search(query)
