import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
import random
import string


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


    def guardar_lista_en_archivo(persona):
        with open("BD_Usuarios1.txt", 'a') as file:
            for persona in range(0,7):
                file.write(', '.join(persona))
                           
    def registro1():
        
        genero = gender.get()
        nombre = name.get()
        apellido = last_name.get()
        ident = id.get()
        nacion = nacionalidad.get()
        cel = telefono.get()
        email = correo.get()
        acum = 0
        if len(ident) == 10:
                acum += 1
        if len(cel) == 10:
            if cel[0] == "3":
                acum += 1
        for i in range(len(email)):
            if email[i] == "@":
                acum += 1
            if email[i] == " ":
                acum -= 1 
        if acum == 3:
            codigo = nombre[0].upper() + '-'
            codigo += ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            global persona
            persona = [genero, nombre, apellido, ident, nacionalidad, cel, correo, codigo]
            guardar_lista_en_archivo(persona)
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
    global gender
    gender = ctk.CTkComboBox(frame2, values = ["Femenino","Masculino","Otro"], bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    gender.place(relx = 0.1, rely = 0.08)
    tkinter.Label(frame2, text = "Genéro", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.175, rely = 0.18)

    #Nombre--Container secundario
    global name
    name = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    name.place(relx = 0.38, rely = 0.08)
    tkinter.Label(frame2, text = "Primer nombre", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.42, rely = 0.18)

    #Apellido--Container secundario
    global last_name
    last_name = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    last_name.place(relx = 0.66, rely = 0.08)
    tkinter.Label(frame2, text = "Primer apellido", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.7, rely = 0.18)

    #Identificacion--Container secundario
    global id
    id = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 250, height = 39)
    id.place(relx = 0.16, rely = 0.31)
    tkinter.Label(frame2, text = "Identificación", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.265, rely = 0.41)

    #Nacionalidad--Container secundario
    global nacionalidad
    nacionalidad = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    nacionalidad.place(relx = 0.56, rely = 0.31)
    tkinter.Label(frame2, text = "Nacionalidad", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.61, rely = 0.41)

    #Boton seleccionar vuelo
    sel_vuelo = ctk.CTkButton(frame2, text = "Seleccionar vuelo", font = ("Garamound", 18), height = 40, width = 130).place(relx = 0.1, rely = 0.55)

    #Telefono--Container secundario
    global telefono
    telefono = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    telefono.place(relx = 0.35, rely = 0.55)
    tkinter.Label(frame2, text = "Teléfono", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.42, rely = 0.65)

    #Correo--Container secundario
    global correo
    correo = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), border_color = "#0B99B9", width = 170, height = 39)
    correo.place(relx = 0.64, rely = 0.55)
    tkinter.Label(frame2, text = "Correo electrónico", fg = "#00576C", bg = "white", font = ("Garamound",13)).place(relx = 0.66, rely = 0.65)

    #Boton continuar
    continuar = ctk.CTkButton(frame2, text = "Continuar", command = registro1, font = ("Garamound", 18), height = 40, width = 300)
    continuar.place(relx = 0.28, rely = 0.77)


    ventana.mainloop()
registro()