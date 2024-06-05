import random
import string
import re

def generar_codigo(nombre):
    codigo = nombre[0].upper() + '-'
    codigo += ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return codigo

def generar_numero_telefonico():
    prefix = random.choice(['301', '302', '304', '305', '315', '316', '317', '318', '320', '321'])
    numero = prefix + ''.join(random.choices(string.digits, k=7))
    return numero

def validar_numero_telefonico(numero):
    return re.fullmatch(r'^3(?:01|02|04|05|15|16|17|18|20|21)\d{7}$') is not None

def validar_correo(correo):
    return re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo) is not None

def generar_lista_persona():
    while True:
        datos = Registro.registro1()
        numero_telefonico = datos[5]
        if validar_numero_telefonico(numero_telefonico):
            break
        else:
            print("El número telefónico no cumple con la estructura especificada. Inténtelo de nuevo.")

    while True:
        correo = input("Ingrese el nombre de usuario del correo electrónico: ")
        if validar_correo(correo):
            break
        else:
            print("El correo electrónico no cumple con la estructura especificada. Inténtelo de nuevo.")

    codigo = generar_codigo(primer_nombre)
    
    persona = [genero, primer_nombre, primer_apellido, numero_documento, nacionalidad, numero_telefonico, correo, codigo]
    return persona

def guardar_lista_en_archivo(lista, archivo):
    with open(archivo, 'a') as file:
        for persona in lista:
            file.write(', '.join(persona) + '\n')


if __name__ == "_main_":
    