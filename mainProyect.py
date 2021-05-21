# Librerias y conexión.
from connect import Connect
from pymongo import MongoClient

# Llamar como conexión objeto.
connection = Connect.get_connection()
db = connection.myFirstDatabase

db.registro.insert_one(
    {"Nombre": "José Luis",
    "Apellido": "Miranda",
    "Edad": 21,
    "CURP": "MILC"})
