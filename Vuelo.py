import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
#Importamos arhivo
import Datos_Vuelo

def vuelos():
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

    #Destino
    tkinter.Label(ventana, text = "Ida: ", bg = "white", font = ("Garamound",18)).place(relx = 0.02, rely = 0.02)

    ventana.mainloop()
