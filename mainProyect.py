# Librerias y conexión.
from connect import Connect
from pymongo import MongoClient
from pprint import pprint

# Llamar como conexión objeto.
connection = Connect.get_connection()
db = connection.myFirstDatabase

db.registro.insert_one(
    {"Nombre": "José Luis",
    "Apellido": "Miranda",
    "Edad": 21,
    "CURP": "MILC"})

cursor = db.registro.find({})

for inventory in cursor:
     pprint(inventory)
