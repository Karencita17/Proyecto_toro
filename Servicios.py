import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox

def servicios():
    ventana = tkinter.Tk() #Crear ventana
    ventana.title("Sky-Voyage") #Titulo
    ventana.configure(bg = "white")
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

    #Container de Aluminio
    frame7 = tkinter.Frame(ventana, width = 450, bg = "white", height = 270, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame7.place(relx = 0.03, rely = 0.03)

    #Titulo Aluminio
    tkinter.Label(frame7, text = "Aluminio",bg = "white", fg = "black",font = ("Berlin Sans FB",18)).place(relx = 0.35, rely = 0.08)

    #Precio Aluminio
    tkinter.Label(frame7, text = "Precio",bg = "white", fg = "black",font = ("Berlin Sans FB",14)).place(relx = 0.41, rely = 0.22)

    #Que incluye
    tkinter.Label(frame7, text = "1 artículo personal (bolso) (Debe caber debajo del asiento)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.34)
    tkinter.Label(frame7, text = "1 equipaje de mano (10 kg) (Desde $195.100 COP)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.44)
    tkinter.Label(frame7, text = "Equipaje de bodega (23 kg) (Desde $175.600 COP)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.54)
    tkinter.Label(frame7, text = "Asiento Economy (Aleatoria-clasificado Aluminio)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.64)
    tkinter.Label(frame7, text = "Cambios de vuelo (No es permitido)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.74)
    tkinter.Label(frame7, text = "Reembolso (No es permitido)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.84)

    #Container de Diamante
    frame8 = tkinter.Frame(ventana, width = 480, bg = "white", height = 270, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame8.place(relx = 0.5, rely = 0.03)

    #Titulo Diamante
    tkinter.Label(frame8, text = "Diamante",bg = "white", fg = "black",font = ("Berlin Sans FB",18)).place(relx = 0.35, rely = 0.08)

    #Precio Diamante
    tkinter.Label(frame8, text = "Precio",bg = "white", fg = "black",font = ("Berlin Sans FB",14)).place(relx = 0.41, rely = 0.22)

    #Que incluye
    tkinter.Label(frame8, text = "1 artículo personal (bolso) (Debe caber debajo del asiento)", bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.34)
    tkinter.Label(frame8, text = "1 equipaje de bodega (23 kg) (Debe caber en el compartimiento superior)", bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.44)
    tkinter.Label(frame8, text = "1 equipaje de mano (10 kg) (Entrega el equipaje en el counter)", bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.54)
    tkinter.Label(frame8, text = "Asiento Economy (Filas específicas disponibles de manera aleatoria)", bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.64)
    tkinter.Label(frame8, text = "Cambios de vuelo (No es permitido)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.74)
    tkinter.Label(frame8, text = "Reembolso (No es permitido)",bg = "white", fg = "black",font = ("Berlin Sans FB",11)).place(relx = 0.01, rely = 0.84)

    ventana.mainloop()

servicios()