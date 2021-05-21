from pymongo import MongoClient

# Conection of BD Online.
class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://cluster0.yhrhg.mongodb.net/myFirstDatabase --username bugsDevelopers")