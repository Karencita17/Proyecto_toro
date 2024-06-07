import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk


def check():
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
    #Icono superior izquierdo
    ventana.iconbitmap("Logos\Avion.ico")

    #Verifica usuario en BD
    def leer_codigo():
        code = codigo.get()
        last_name = apellido.get()
        with open("BD_Usuarios1.txt", "r") as archivo:
            usuario = archivo.read()
            usuario = usuario.split(",")
            contador = 0
            for i in range(0,len(usuario)):
                if usuario[i] == last_name:
                    contador+=1
            for j in range(0,len(usuario)):
                if usuario[j] == code:
                    contador+=1
            if contador ==2:
                tkinter.Label(frame, text = "Este usuario esta en la BD", fg = "red", bg = "white", font = ("Garamoun",14)).place(relx=0.3,rely=0.74)
            else:
                tkinter.Label(frame, text = "Este usuario no se encuentra", fg = "red", bg = "white", font = ("Garamoun",14)).place(relx=0.3,rely=0.74)

    
    #Tema predeterminado
    ctk.set_default_color_theme("blue")

    #Container 
    frame = tkinter.Frame(ventana, width = 600, height = 550, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

    #Logo Check-in
    avion = ctk.CTkImage(Image.open(fr"Logos\Logo_check.png"), size = (120,120))
    text = ctk.CTkLabel(master = frame, image = avion, text = "")
    text.place(relx=0.5,rely=0.23, anchor=tkinter.CENTER)

    #Pedimos codigo
    text1 = tkinter.Label(frame, text = "Código: ", bg = "White", fg = "#006D87", font = ("Garamoun",14))
    text1.place(relx=0.33,rely=0.41, anchor=tkinter.CENTER)
    codigo = ctk.CTkEntry(frame, width = 300, height = 38, font = ("Arial",17),  border_color = "#0B99B9")
    codigo.place(relx=0.5,rely=0.48, anchor=tkinter.CENTER)

    #Pedimos apellido
    text2 = tkinter.Label(frame, text = "Apellido: ", bg = "White", fg = "#006D87", font = ("Garamoun",14))
    text2.place(relx=0.33,rely=0.61, anchor=tkinter.CENTER)
    apellido = ctk.CTkEntry(frame, width = 300, height = 38, font = ("Arial",17), border_color = "#0B99B9")
    apellido.place(relx=0.5,rely=0.67, anchor=tkinter.CENTER)

    #Boton verificar
    verificar = ctk.CTkButton(frame, text = "Verificar", fg_color = "#0B99B9", command = leer_codigo, font = ("Garamond",22), height = 40, width = 130)
    verificar.place(relx=0.5,rely=0.85, anchor=tkinter.CENTER)

    ventana.mainloop()
check()