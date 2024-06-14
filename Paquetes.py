import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
import Asientos
import Resumen_compra
import random

def paquetes():
    ventana3 = tkinter.Tk() #Crear ventana
    ventana3.title("Sky-Voyage") #Titulo
    ventana3.configure(bg = "white")
    #Imagen de fondo
    fondo = ctk.CTkImage(Image.open(fr"Logos\fondo.png"), size=(1535, 795))
    text = ctk.CTkLabel(master = ventana3, image = fondo, text = "")
    text.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
    #Centrar la ventana tamaño pc
    ventana3_width=1000
    ventana3_height=650
    ventana3.resizable(0,0)
    screen_width=ventana3.winfo_screenwidth()
    screen_height=ventana3.winfo_screenheight()
    x=(screen_width/2)-(ventana3_width/2)
    y=(screen_height/2)-(ventana3_height/2)
    ventana3.geometry(f'{ventana3_width}x{ventana3_height}+{int(x)}+{int(y)}')
    #Icono superior izquierdo
    ventana3.iconbitmap("Logos\Avion.ico")

    #Tema predeterminado
    ctk.set_default_color_theme("blue")


    def escoge_aluminio(asiento):
        letras = ["A", "B", "C", "D", "E", "F"]
        numeros = [9, 10, 11, 12]
        asiento = random.choice(letras) +"-" +random.choice(numeros)
        x = aluminio.cget("text")
        with open(fr"BD_Usuarios1.txt", 'a') as file:
            mensaje = ""
            mensaje += str(x) +"," +asiento
            file.write(mensaje)
        ventana3.destroy()
        Resumen_compra.resumen_de_la_compra()

    def escoge_diamante():
        letras = ["A", "B", "C", "D", "E", "F"]
        numeros = [5, 6, 7, 8]
        asiento = random.choice(letras) +"-" +str(random.choice(numeros))
        y = diamante.cget("text")
        with open(fr"BD_Usuarios1.txt", 'a') as file:
            mensaje = ""
            mensaje += str(y) +"," +asiento
            file.write(mensaje)
        ventana3.destroy()
        Resumen_compra.resumen_de_la_compra()

    def escoge_premium():
        z = premium.cget("text")
        with open(fr"BD_Usuarios1.txt", 'a') as file:
            mensaje = ""
            mensaje += str(z) +","
            file.write(mensaje) 
        ventana3.destroy()
        Asientos.abrir_ventana_seleccion_asientos()
        

    frame = tkinter.Frame(ventana3, bg = "white", width = 600, height = 50, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
    frame.place(relx = 0.2, rely = 0.03)

    tkinter.Label(ventana3, bg = "white", text = "Nuestros Servicios", font = ("Berlin Sans FB",23), fg = "#00576C").place(relx=0.5, rely=0.07, anchor=tkinter.CENTER)

    frame1 = tkinter.Frame(ventana3, bg = "white", width = 300, height = 500, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
    frame1.place(relx = 0.02, rely = 0.16)

    #Paquete Aluminio
    aluminio = tkinter.Label(frame1, text="Aluminio", font = ("Berlin Sans FB",20), bg = "white")
    aluminio.place(relx=0.32, rely=0.03)

    tkinter.Label(frame1, text = " 1 artículo personal (bolso) \n (Debe caber debajo del asiento)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.12, rely=0.13)
    tkinter.Label(frame1, text = " 1 equipaje de mano (10 kg) \n (Desde $195.100 COP)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.16, rely=0.25)
    tkinter.Label(frame1, text = " Equipaje de bodega (23 kg) \n (Desde $175.600 COP)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.17, rely=0.37)
    tkinter.Label(frame1, text = " Asiento Economy \n (Aleatoria-clasificado Aluminio)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.12, rely=0.49)
    tkinter.Label(frame1, text = " Cambios de vuelo \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.61)
    tkinter.Label(frame1, text = " Reembolso \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.74)

    seleccionar1 = ctk.CTkButton(frame1, text = "Seleccionar", height = 35, font = ("Berlin Sans FB",17), command = escoge_aluminio)
    seleccionar1.place(relx = 0.26, rely = 0.88)


    frame2 = tkinter.Frame(ventana3, bg = "white", width = 300, height = 500, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
    frame2.place(relx = 0.35, rely = 0.16)

    #Paquete Diamante
    diamante = tkinter.Label(frame2, text="Diamante", font = ("Berlin Sans FB",20), bg = "white")
    diamante.place(relx=0.31, rely=0.03)

    tkinter.Label(frame2, text = " 1 artículo personal (bolso) \n (Debe caber debajo del asiento)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.13, rely=0.13)
    tkinter.Label(frame2, text = " 1 equipaje de bodega (23 kg) (Debe \n caber en el compartimiento superior)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.08, rely=0.25)
    tkinter.Label(frame2, text = " 1 equipaje de mano (10 kg) \n (Entrega el equipaje en el counter)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.11, rely=0.37)
    tkinter.Label(frame2, text = " Asiento Economy (Filas específicas \n disponibles de manera aleatoria)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.1, rely=0.49)
    tkinter.Label(frame2, text = " Cambios de vuelo \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.61)
    tkinter.Label(frame2, text = " Reembolso \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.74)

    seleccionar2 = ctk.CTkButton(frame2, text = "Seleccionar", height = 35, font = ("Berlin Sans FB",17), command = escoge_diamante)
    seleccionar2.place(relx = 0.26, rely = 0.88)
                        

    frame3 = tkinter.Frame(ventana3, bg = "white", width = 300, height = 500, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
    frame3.place(relx = 0.68, rely = 0.16)

    #Paquete Premium
    premium = tkinter.Label(frame3, text="Premium", font = ("Berlin Sans FB",20), bg = "white")
    premium.place(relx=0.33, rely=0.03)

    tkinter.Label(frame3, text = " 1 artículo personal (bolso) \n (Debe caber debajo del asiento)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.13, rely=0.13)
    tkinter.Label(frame3, text = " 1 equipaje de mano (10 kg) (Debe \n caber en el compartimiento superior)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.09, rely=0.25)
    tkinter.Label(frame3, text = " 1 equipaje de bodega (23 kg) \n (Entrega el equipaje en el counter)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.11, rely=0.37)
    tkinter.Label(frame3, text = " Asiento Plus (Sujeto \n a disponibilidad-clasificado Premium)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.09, rely=0.49)
    tkinter.Label(frame3, text = " Cambios de vuelo \n (Sin cargo por cambio, antes del vuelo)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.07, rely=0.61)
    tkinter.Label(frame3, text = " Reembolso \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.74)

    seleccionar3 = ctk.CTkButton(frame3, text = "Seleccionar", height = 35, font = ("Berlin Sans FB",17), command = escoge_premium)
    seleccionar3.place(relx = 0.27, rely = 0.88)

    ventana3.mainloop()