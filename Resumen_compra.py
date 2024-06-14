import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
import Pagar_vuelo

def resumen_de_la_compra():
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

    def realizar_pago():
        ventana.destroy()
        Pagar_vuelo.pagar()

    #Titulo Bienvenida
    text1 = tkinter.Label(ventana, text = "Resumen de la compra", bg = "White", fg = "#0B99B9", font = ("Garamond",33))
    text1.place(relx=0.5,rely=0.1, anchor=tkinter.CENTER)

    with open("BD_Usuarios1.txt", "r") as archivo: 
        info_vuelos = archivo.readlines()
    #Se toma la ultima fila
    ultimo = info_vuelos[-1]
    ultimo = ultimo.split(",") #Se omiten ,
    for i in range(len(ultimo)):
        frame = tkinter.Frame(ventana, width = 800, height = 50, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
        frame.place(relx=0.11, rely=0.2)

        tkinter.Label(frame, text = ultimo[0].upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.01, rely=0.16)
             
        tkinter.Label(frame, text = "(" +ultimo[3] +")", width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.09, rely=0.16)

        tkinter.Label(frame, text = "-----------------------------------------------", width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.21, rely=0.16)
                 
        tkinter.Label(frame, text = ultimo[1].upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.34, rely=0.16)
             
        tkinter.Label(frame, text = "(" +ultimo[4] +")", width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.44, rely=0.16)
            
        tkinter.Label(frame, text = "Desde:  ", width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.54, rely=0.16)
            
        tkinter.Label(frame, text = "COP. " +ultimo[5], width = 10, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.65, rely=0.16)

        plan = tkinter.Label(frame, text = ultimo[16], width = 10, bg = "white", font = ("Berlin Sans FB",14), fg = "#0B99B9",)
        plan.place(relx=0.82, rely=0.16)

        tkinter.Label(ventana, text = "Total a pagar: ", fg = "#0B99B9", bg = "white", font = ("Berlin Sans FB",23)).place(relx=0.53, rely=0.8)

        plan1 = plan.cget("text")
        if plan1 == "Aluminio":
            tkinter.Label(ventana, text = "COP. " +ultimo[5], bg = "white", font = ("Berlin Sans FB",16)).place(relx=0.75, rely=0.81)
        elif plan1 == "Diamante":
            tkinter.Label(ventana, text = "COP. " +ultimo[6], bg = "white", font = ("Berlin Sans FB",16)).place(relx=0.75, rely=0.81)
        elif plan1 == "Premium":
            tkinter.Label(ventana, text = "COP. " +ultimo[7], bg = "white", font = ("Berlin Sans FB",16)).place(relx=0.75, rely=0.81)

    #Boton continuar
    continuar = ctk.CTkButton(ventana, text = "Continuar", fg_color = "#0B99B9", font = ("Garamond",22), height = 40, width = 110, command = realizar_pago)
    continuar.place(relx=0.9,rely=0.93, anchor=tkinter.CENTER)


    ventana.mainloop()
