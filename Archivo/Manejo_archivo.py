def write(): #Escribir texto en archivo
    name = ["Karen","Nicolas","Sebastian","Camilo","Pablo","Vito"] #Lista de datos
    with open("names.txt", "w") as file:  #Creación y apertura
        for i in name:
            file.write(i + "\n")   #Se añade la lista a names.txt
    file.close()  #Se tiene que cerrar 


def read():   #Txt a Lista
    listname = []
    with open("names.txt", "r") as file:  #Se lee el txt
        for i in file:
            listname.append(i)  #Se añade a la lista
    file.close()
    print(listname)

read()