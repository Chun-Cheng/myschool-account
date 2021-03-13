import pymongo
from bson.objectid import ObjectId
import re

client = pymongo.MongoClient('mongodb+srv://dbUser:o5jzqcHzuKacB2Y1@lunchbox.1pvyu.mongodb.net/lunchbox?retryWrites=true&w=majority')
database = client.account

class DB_MODEL:
    def __init__(self):
        self.db = database
        
    def create(self):
        data = {}
        res = database.insert_one(data)
        return str(res.inserted_id)
    
    def find(self, query, sendback):
        """
        input:
          query:dict,{column_name:data_value}
          sendback:string list,what column do you want to fetch
        output:
          list
        """
        columns = {}
        if '_id' not in sendback:
            columns['_id'] = 0
        for i in sendback:
            columns[i] = 1
        return list(self.db.find(query, columns))
    
    def update_one(self, query, new_value):
        """
        input:
          query:dict,{column_name:data_value}
          new_value:dict,{modify_method:{column_name:update_content}}
        output:
          None
        """
        self.db.update_one(query, new_value)
        return None
    
    def update_many(self, query, new_value):
        res = self.db.update_many(query, new_value)
        return res.modified_count
    
    def delete_one(self, query):
        """
        input:
          query:dict,{column_name:data_value}
        output:
          None
        """
        self.db.delete_one(query)
        return None
    
    def delete_many(self, query):
        """
        input:
          query:dict,{column_name:data_value}
        output:
          delete_count:integer
        """
        res = self.db.delete_many(query)
        return res.deleted_count


class SSO(DB_MODEL):
    def __init__(self):
        pass
    def create(self):
        pass
    def find(self):
        pass
     
