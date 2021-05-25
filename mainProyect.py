# Librerias y conexión.
from connect import Connect
from pymongo import MongoClient
from pprint import pprint

# Llamar como conexión objeto.
connection = Connect.get_connection()
db = connection.myFirstDatabase

def insertarReg():
    print("--- Registro ---")
    id = int(input("Inserta ID: "))
    name = input("Inserta Nombre: ")
    lastname = input("Inserta Apellido: ")
    year = int(input("Inserta Edad: "))
    folio = int(input("Inserta Folio: "))
    print()

    db.vacune.insert_one(
        {"Indice": id,
        "Nombre": name,
        "Apellido": lastname,
        "Edad": year,
        "CURP": folio})

    consultarReg()
    # --> Necesitamos obtener la información de la collección para
    # pegarlos en XML.
    print()

def actualizarReg():
    print("Hola!")
    # Actualizara la información de un registro.
    '''
    db.register.update_one(
        {"name": "Guuz"},
        {"$set": {"lastname": "Aniseto"},
        "$currentDate": {"lastModified": True}})
    print("Actualización correctamente.")
    '''
    # consultarReg()
    # --> Necesitamos obtener la información de la collección para
    # pegarlos en XML.

def eliminarReg():
    # Eliminará el dato que tenga el mismo nombre de dicha variable.
    indice = int(input("Inserte indice >> "))
    db.vacune.delete_one({"Indice": indice})
    print("Registro eliminado!\n")
    # consultarReg()
    # --> Necesitamos obtener la información de la collección para
    # pegarlos en XML.

def consultarReg():
    regs = db.vacune.find({})
    for inventory in regs:
        pprint(inventory)

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

'''
# Funcion que crea el documento XML con formato.
def crearXML():
    # Crear la estructura del archivo
    data = arch.Element('Abarroteria')
    xd = len(namesArray)
    for i in range(xd):
        items = arch.SubElement(data, 'items')
        item1 = arch.SubElement(items, 'id')
        item2 = arch.SubElement(items, 'name')
        item3 = arch.SubElement(items, 'lastname')
        item4 = arch.SubElement(items, 'year')
        item5 = arch.SubElement(items, 'folio')
        
    # Crear el archivo XML y abrir tal archivo.
    mydata = arch.ElementTree(data)
    mydata.write("archivo.xml")

# Función que lee el archivo XML e imprime lo que tiene en consola.
def leerArch():
    print("--- Lectura ---")
    if os.path.isfile("archivo.xml"):
        if os.stat("archivo.xml").st_size==0:
            print("El archivo está vacio, debe llenarse!")
            print()
        else:
            xml = minidom.parse("archivo.xml")
            docs = xml.getElementsByTagName("items")
            print("{:<5} {:<10} {:<6} {:<3} {:<6}".format('ID', 'Nombre', 'Apellido', 'Edad', 'Folio'))
            for items in docs:
                id = items.getElementsByTagName("id")[0]
                name = items.getElementsByTagName("name")[0]
                lastname = items.getElementsByTagName("lastname")[0]
                year = items.getElementsByTagName("year")[0]
                folio = items.getElementsByTagName("folio")[0]
                print("{:<5} {:<10} {:<6} {:<3}".format(id.firstChild.data, name.firstChild.data, lastname.firstChild.data, year.firstChild.data, folio.firstChild.data))
            print()
    else:
        print("El archivo de registro no existe.")
        print()
'''