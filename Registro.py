import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import Paquetes

def guardar_lista_en_archivo(lista, archivo):
        #Abrimos archivo txt para añadir y le damos un sobrenombre
        with open(archivo, 'a') as file:
            mensaje = ""
            for dato in range(len(lista)):
                if dato != len(lista):
                    mensaje += str(lista[dato]) + ","
            file.write(mensaje)
                           
def registro():
    ventana = tkinter.Tk() #Crear ventana
    ventana.title("Sky-Voyage") #Titulo
    ventana.configure(bg="white")
    #Imagen de fondo
    fondo = ctk.CTkImage(Image.open(fr"Logos\fondo.png"), size=(1573, 795))
    text3 = ctk.CTkLabel(master = ventana, image = fondo, text = "")
    text3.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
    #Centrar la ventana tamaño pc
    ventana_width=1000
    ventana_height=650
    ventana.resizable(0,0)
    screen_width=ventana.winfo_screenwidth()
    screen_height=ventana.winfo_screenheight()
    x=(screen_width/2)-(ventana_width/2)
    y=(screen_height/2)-(ventana_height/2)
    ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')
    ventana.iconbitmap("Logos\Avion.ico")
    
    def registro1():
        #Se obtienen datos
        genero = gender.get()
        nombre = name.get()
        apellido = last_name.get()
        nacion = nacionalidad.get()
        email = correo.get()
        try:
            if genero == "" or nombre == "" or apellido == "" or nacion == "" or email == "": #Si los campos estan vacios se genera un error
                raise ValueError
        except ValueError:
            #Mensaje de error, se pide la informaación completa
            messagebox.showinfo(message="Por favor, complete los campos", title="Error")
        else:
            #Si los datos son negativos genera error
            try:
                #Verifica que sea entero
                cel = int(telefono.get()) 
                if cel <= 0:
                    raise ValueError
            except:
                messagebox.showinfo(message="Número incorrecto", title="Error")
            try:
                #Verifica que sea entero
                ident = int(id.get())
                if ident <= 0:
                    raise ValueError
            except:
                messagebox.showinfo(message="Identidad incorrecta", title="Error")
            else:
                #Numeros validos en Colombia
                numeros_validos = ["300", "301", "302", "303", "304", "305", "310", "311", "312", "313", "314" "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "333", "350", "351"]
                acum = 0
                #Verifica que tenga 10 digitos el numero de identidad
                if len(str(ident)) == 10:
                        acum += 1
                #Verifica que tenga 10 digitos el telefono celular
                if len(str(cel)) == 10:
                    for i in range(len(numeros_validos)):
                        #Verifica que cumpla con la estructura valida
                        if str(cel)[0:3] == numeros_validos[i]:
                            acum += 1
                #Verifica Email
                for i in range(len(email)):
                    #Verifica que este el @
                    if email[i] == "@":
                        acum += 1
                    #Verifica que no haya espacios
                    if email[i] == " ":
                        acum -= 1 
                #Al cumplirse todas las condiciones, pasa
                if acum == 3:
                    #Genera codigo aleatoriamente
                    codigo = nombre[0].upper() + '-'
                    #Letras del abecedario
                    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    for i in range(1,4):
                        codigo += str(random.randint(1,9)) +random.choice(abc) 
                    #Se almacena en una lista
                    persona = [genero, nombre, apellido, str(ident), nacion, str(cel), email, codigo]
                    #Llamamos funcion para guardar en txt
                    guardar_lista_en_archivo(persona,fr"BD_Usuarios1.txt")
                    ventana.destroy()
                    Paquetes.paquetes()
                else:
                    tkinter.Label(frame, text = "Por favor, verifique la información", fg = "red", bg = "white", font = ("Garamound",12)).place(relx = 0.5, rely = 0.95, anchor=tkinter.CENTER)

    #Container principal
    frame = tkinter.Frame(ventana, bg = "white", width = 740, height = 570, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame.place(relx = 0.5, rely = 0.5, anchor=tkinter.CENTER)

    #Titulo, Logo--Container principal
    tkinter.Label(frame, text = "Registro", fg = "#00576C", bg = "white", font = ("Garamound",31)).place(relx = 0.45, rely = 0.13, anchor=tkinter.CENTER)
    registro = ctk.CTkImage(Image.open(fr"Logos\registered.png"), size=(100, 100))
    text3 = ctk.CTkLabel(master = frame, image = registro, text = "")
    text3.place(relx=0.7,rely=0.13, anchor=tkinter.CENTER)

    #Container secundario
    frame2 = tkinter.Frame(frame, bg = "white", width = 740, height = 433, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame2.place(relx = 0.5, rely = 0.62, anchor=tkinter.CENTER) 

    #Genero--Container secundario
    gender = ctk.CTkComboBox(frame2, values = ["Femenino","Masculino","Otro"], bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    gender.place(relx = 0.1, rely = 0.08)
    tkinter.Label(frame2, text = "Genéro", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.175, rely = 0.18)

    #Nombre--Container secundario
    name = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    name.place(relx = 0.38, rely = 0.08)
    tkinter.Label(frame2, text = "Primer nombre", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.42, rely = 0.18)

    #Apellido--Container secundario
    last_name = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    last_name.place(relx = 0.66, rely = 0.08)
    tkinter.Label(frame2, text = "Primer apellido", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.7, rely = 0.18)

    #Identificacion--Container secundario
    id = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 250, height = 39)
    id.place(relx = 0.16, rely = 0.31)
    tkinter.Label(frame2, text = "Identificación", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.265, rely = 0.41)

    #Nacionalidad--Container secundario
    nacionalidad = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    nacionalidad.place(relx = 0.56, rely = 0.31)
    tkinter.Label(frame2, text = "Nacionalidad", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.61, rely = 0.41)

    #Telefono--Container secundario
    telefono = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    telefono.place(relx = 0.23, rely = 0.55)
    tkinter.Label(frame2, text = "Teléfono", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.3, rely = 0.65)

    #Correo--Container secundario
    correo = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    correo.place(relx = 0.54, rely = 0.55)
    tkinter.Label(frame2, text = "Correo electrónico", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.56, rely = 0.65)

    #Boton continuar
    continuar = ctk.CTkButton(frame2, text = "Continuar", command = registro1, font = ("Garamound", 18), height = 40, width = 300)
    continuar.place(relx = 0.28, rely = 0.77)


    ventana.mainloop()