import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
import Registro
from tkinter import messagebox
import Paquetes

def registrado_check():
    ventana = tkinter.Tk() #Crear ventana
    ventana.title("Sky-Voyage") #Titulo
    ventana.configure(bg = "White")  
    #Centrar la ventana tamaño pc
    ventana_width=1000
    ventana_height=650
    ventana.resizable(0,0)
    screen_width=ventana.winfo_screenwidth()
    screen_height=ventana.winfo_screenheight()
    x=(screen_width/2)-(ventana_width/2)
    y=(screen_height/2)-(ventana_height/2)
    ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')
    #Icono superior izquierdo
    ventana.iconbitmap("Logos\Avion.ico") 

    #Tema predeterminado
    ctk.set_default_color_theme("blue")

    #Registrarse
    def querer_registrar():
        ventana.destroy()
        Registro.registro()

    #Hacer check-in
    def check_in():
        ventana.destroy()
        ventana1 = tkinter.Tk() #Crear ventana1
        ventana1.title("Sky-Voyage") #Titulo
        ventana1.configure(bg="white") #Color de fondo
        #Imagen de fondo
        fondo = ctk.CTkImage(Image.open(fr"Logos\fondo.png"), size=(1573, 795))
        text3 = ctk.CTkLabel(master = ventana1, image = fondo, text = "")
        text3.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
        #Centrar la ventana1 tamaño pc
        ventana1_width=1000
        ventana1_height=650
        ventana1.resizable(0,0)
        screen_width=ventana1.winfo_screenwidth()
        screen_height=ventana1.winfo_screenheight()
        x=(screen_width/2)-(ventana1_width/2)
        y=(screen_height/2)-(ventana1_height/2)
        ventana1.geometry(f'{ventana1_width}x{ventana1_height}+{int(x)}+{int(y)}')
        #Icono superior izquierdo
        ventana1.iconbitmap("Logos\Avion.ico")

        #Verifica usuario en BD
        def leer_codigo():
            #Se obtienen datos
            code = codigo.get()
            last_name = apellido.get()

            try:
                if code == "" or last_name == "": #Si los campos estan vacios se genera un error
                    raise ValueError
            except ValueError:
                #Mensaje de error, se pide la informaación completa
                messagebox.showinfo(message="Por favor, complete los campos", title="Error")
            else:
                #Abrimos archivo txt para leer y le damos un sobrenombre
                with open("BD_Usuarios1.txt", "r") as archivo:
                    #Al leer se almacena en la variable usuario
                    usuario = archivo.read()
                    usuario = usuario.split(",")
                    contador = 0
                    #Recorre usuario, o sea BD_Usuarios
                    for i in range(len(usuario)):
                        if usuario[i] == last_name:
                            contador+=1
                    for j in range(len(usuario)):
                        if usuario[j] == code:
                            contador+=1
                    if contador ==2:
                        Paquetes.paquetes()
                    else:
                        tkinter.Label(frame, text = "Este usuario no se encuentra", fg = "red", bg = "white", font = ("Garamoun",14)).place(relx=0.3,rely=0.74)

    
        #Tema predeterminado
        ctk.set_default_color_theme("blue")

        #Container 
        frame = tkinter.Frame(ventana1, width = 600, height = 550, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
        frame.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

        #Logo Check-in
        avion = ctk.CTkImage(Image.open(fr"Logos\Logo_check.png"), size = (120,120))
        text = ctk.CTkLabel(master = frame, image = avion, text = "")
        text.place(relx=0.5,rely=0.23, anchor=tkinter.CENTER)

        #Codigo-----Entry y Label
        text1 = tkinter.Label(frame, text = "Código: ", bg = "White", fg = "#006D87", font = ("Garamoun",14))
        text1.place(relx=0.33,rely=0.41, anchor=tkinter.CENTER)
        codigo = ctk.CTkEntry(frame, width = 300, height = 38, font = ("Arial",17),  border_color = "#0B99B9")
        codigo.place(relx=0.5,rely=0.48, anchor=tkinter.CENTER)

        #Apellido-----Entry y Label
        text2 = tkinter.Label(frame, text = "Apellido: ", bg = "White", fg = "#006D87", font = ("Garamoun",14))
        text2.place(relx=0.33,rely=0.61, anchor=tkinter.CENTER)
        apellido = ctk.CTkEntry(frame, width = 300, height = 38, font = ("Arial",17), border_color = "#0B99B9")
        apellido.place(relx=0.5,rely=0.67, anchor=tkinter.CENTER)

        #Boton verificar
        verificar = ctk.CTkButton(frame, text = "Verificar", fg_color = "#0B99B9",command = leer_codigo, font = ("Garamond",22), height = 40, width = 130)
        verificar.place(relx=0.5,rely=0.85, anchor=tkinter.CENTER)

        ventana1.mainloop()

    #Foto rasgada a la mitad
    fondo_rasgado = ctk.CTkImage(Image.open(fr"Logos\fondo_rasgado.jpg"), size=(1000, 700))
    text = ctk.CTkLabel(master = ventana, image = fondo_rasgado, text = "")
    text.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

    #Titulo Sky-Voyage
    text1 = tkinter.Label(ventana, text = "Sky-Voyage", bg = "#F7F7F7", fg = "#005E75", font = ("Garamond",63))
    text1.place(relx=0.3,rely=0.15, anchor=tkinter.CENTER)

    #Subtitulo 
    text2 = tkinter.Label(ventana, text = "¿Ya tienes una cuenta?", bg = "#F7F7F7", font = ("Garamond",16))
    text2.place(relx=0.3,rely=0.27, anchor=tkinter.CENTER)

    #Boton Inicio_sesion
    inicio_sesion = ctk.CTkButton(ventana, text = "Iniciar Sesión", fg_color = "#0B99B9", font = ("Garamond",22), height = 40, width = 130, command = check_in)
    inicio_sesion.place(relx=0.19,rely=0.39, anchor=tkinter.CENTER)

    #Boton Registro
    registrar = ctk.CTkButton(ventana, text = "Registrar", fg_color = "#0B99B9", font = ("Garamond",22), height = 40, width = 130, command = querer_registrar)
    registrar.place(relx=0.41,rely=0.39, anchor=tkinter.CENTER)

    ventana.mainloop()