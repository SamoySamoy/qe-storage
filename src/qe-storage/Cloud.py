from Database import Database
from pymongo import MongoClient

class Cloud(Database):
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
    
    def create_table(self, table_name):
        # In MongoDB, collections are created implicitly when data is inserted.
        pass
    
    def insert(self, table_name, data):
        collection = self.db[table_name]
        collection.insert_one(data)
    
    def update(self, table_name, query, data):
        collection = self.db[table_name]
        collection.update_many(query, {"$set": data})
    
    def delete(self, table_name, query):
        collection = self.db[table_name]
        collection.delete_many(query)
    
    def query(self, table_name, query):
        collection = self.db[table_name]
        return collection.find(query)