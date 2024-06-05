from io import open

#---------Write----------
archivo_texto = open("America.txt", "w")

text = "America campeon"

archivo_texto.write(text)

archivo_texto.close()

#----------Read--------------
archivo_texto2 = open("America.txt", "r")

text2 = archivo_texto2.read()

text2 = archivo_texto2.readline() #Solo una linea

text2 = archivo_texto2.readlines() #Todas las lineas en una lista

print(text2)

#print(archivo_texto2.read()) #Otro metodo