from pymongo import MongoClient

# Conection of BD Online.
class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://bugsDevelopers:12345@cluster0.z1tfi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")