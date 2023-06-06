from abc import ABC, abstractmethod

class Database(ABC):
    
    @abstractmethod
    def create_table(self, table_name):
        pass
    
    @abstractmethod
    def insert(self, table_name, data):
        pass
    
    @abstractmethod
    def update(self, table_name, query, data):
        pass
    
    @abstractmethod
    def delete(self, table_name, query):
        pass
    
    @abstractmethod
    def query(self, table_name, query):
        pass
