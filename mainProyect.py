# Librerias y conexión.
from connect import Connect
from pymongo import MongoClient
from pprint import pprint

import xml.etree.ElementTree as xmlW
from xml.dom import minidom as xmlR

# Llamar como conexión objeto.
connection = Connect.get_connection()
db = connection.myFirstDatabase

def insertarReg():
    print("--- Registro ---")
    id = int(input("Inserta ID: "))
    name = input("Inserta Nombre: ")
    lastname = input("Inserta Apellido: ")
    year = int(input("Inserta Edad: "))
    serie = int(input("Inserta Folio: "))
    print()
    db.vacune.insert_one(
        {"Indice": id,
        "Nombre": name,
        "Apellido": lastname,
        "Edad": year,
        "Folio": serie})
    consultarReg()
    print()

def actualizarReg():
    # Actualizara la información de un registro.
    print("--- Actualizar ---")
    indice = int(input("Inserte indice >> "))
    if db.vacune.find({"Indice" : indice}):
        name = input("Inserta Nombre: ")
        lastname = input("Inserta Apellido: ")
        year = int(input("Inserta Edad: "))
        serie = int(input("Inserta Folio: "))
        print()
        db.register.update_one(
            {"Indice": indice},
            {"$set": {
                "Nombre": name,
                "Apellido": lastname,
                "Edad": year,
                "Folio": serie},
            "$currentDate": {"lastModified": True}})
        print("Actualización correctamente.")
        consultarReg()
    elif db.vacune.find({"Indice" : indice}) == 0:
        print("No existe ningun registro!")
        print()

def eliminarReg():
    print("--- Eliminar ---")
    # Eliminará el dato que tenga el mismo nombre de dicha variable.
    indice = int(input("Inserte indice >> "))
    if db.vacune.find({"Indice" : indice}):
        db.vacune.delete_one({"Indice": indice})
        print("Registro eliminado!\n")
        consultarReg()
        print()
    elif db.vacune.find({"Indice" : indice}) == 0:
        print("No existe ningun registro!")
        print()

def consultarReg():
    regs = db.vacune.find({})
    # Este for se puede comentar para no mostrar nada en pantalla xd
    for inventory in regs:
        print(inventory)
        str(inventory["Indice"])
        str(inventory["Nombre"])
        str(inventory["Apellido"])
        str(inventory["Edad"])
        str(inventory["Folio"])
    escribirArchivo()

def guardarXML(data):
    mydata = xmlW.ElementTree(data)
    mydata.write("archivo.xml")
    print()

def escribirArchivo():
    registros = db.vacune.find({})
    data = xmlW.Element('Abarroteria')
    for inventario in registros:
        item = xmlW.SubElement(data, "item")
        item1 = xmlW.SubElement(item, "Indice")
        item2 = xmlW.SubElement(item, "Nombre")
        item3 = xmlW.SubElement(item, "Apellido")
        item4 = xmlW.SubElement(item, "Edad")
        item5 = xmlW.SubElement(item, "Folio")

        item1.text = str(inventario["Indice"])
        item2.text = str(inventario["Nombre"])
        item3.text = str(inventario["Apellido"])
        item4.text = str(inventario["Edad"])
        item5.text = str(inventario["Folio"])
    guardarXML(data)

# Funcion Menu
def menu():
    print("Hola, Que deseas hacer?")
    print("1. Agregar Registro.")
    print("2. Actualizar Registro.")
    print("3. Eliminar Registro.")
    print("4. Consultar Registros.")
    print("5. Salir")

# Funcion principal que acciona las funciones.
def main():
    while True:
        # Mostramos el menu
        menu()
        opcionMenu = int(input("Inserta un valor >> "))
        print()
        if opcionMenu==1:
            insertarReg()
        elif opcionMenu==2:
            actualizarReg()
        elif opcionMenu==3:
            eliminarReg()
        elif opcionMenu==4:
            consultarReg()
        elif opcionMenu==5:
            print("Hasta Luego!")
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\n")

# Inicio del programa.
main()