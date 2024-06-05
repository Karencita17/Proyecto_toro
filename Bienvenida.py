import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
#Importamos archivos
import Check_in
import Datos_Vuelo


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

#Cambio ventana Check-In
def cambio_check():
    ventana.destroy()
    Check_in.check()

#Cambio ventana Vuelos
def cambio_vuelos():
    ventana.destroy()
    Datos_Vuelo.datos()


#Titulo Bienvenida
text1 = tkinter.Label(ventana, text = "Bienvenido a Sky-Voyage", bg = "White", fg = "#0B99B9", font = ("Garamond",33))
text1.place(relx=0.5,rely=0.2, anchor=tkinter.CENTER)

#Subtitulo 
text2 = tkinter.Label(ventana, text = "¿Qué deseas hacer?", bg = "White", font = ("Garamond",16))
text2.place(relx=0.5,rely=0.3, anchor=tkinter.CENTER)

#Logo Check-in
logo_check = ctk.CTkImage(Image.open(fr"Logos\Logo_check.png"), size=(100, 100))
text = ctk.CTkLabel(master = ventana, image = logo_check, text = "")
text.place(relx=0.4,rely=0.5, anchor=tkinter.CENTER)

#Logo Vuelos
logo_Vuelos = ctk.CTkImage(Image.open(fr"Logos\Vuelos.png"), size=(100, 100))
text3 = ctk.CTkLabel(master = ventana, image = logo_Vuelos, text = "")
text3.place(relx=0.6,rely=0.5, anchor=tkinter.CENTER)

#Boton Check-in
button_check = ctk.CTkButton(ventana, text = "Check-In", command = cambio_check, font = ("Garamond",20), fg_color = "#0B99B9")
button_check.place(relx=0.4,rely=0.63, anchor=tkinter.CENTER)

#Boton Vuelos
button_Vuelos = ctk.CTkButton(ventana, text = "Vuelos", command = cambio_vuelos, font = ("Garamond",20), fg_color = "#0B99B9")
button_Vuelos.place(relx=0.6,rely=0.63, anchor=tkinter.CENTER)

ventana.mainloop()