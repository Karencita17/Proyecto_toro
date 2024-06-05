import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
#Importamos archivo
import Vuelo

def datos():
    ventana = tkinter.Tk() #Crear ventana
    ventana.title("Sky-Voyage") #Titulo
    ventana.configure(bg = "white")
    #Imagen de fondo
    fondo = ctk.CTkImage(Image.open(fr"Logos\fondo.png"), size=(1535, 795))
    text = ctk.CTkLabel(master = ventana, image = fondo, text = "")
    text.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
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

    def datos_buscar():
        inicio = origen.get()
        fin = destino.get()
        dia = fecha.get()
        vuelos = []
        acum = 0
        with open("BD_Vuelos.txt", "r") as archivo:
            usuario = archivo.read()
            usuario = usuario.split("\n")
            for i in range(len(usuario)):
                vuelo = usuario[i].split(",")
                vuelo = [dato.strip().strip("'") for dato in vuelo]
                vuelos.append(vuelo)
        for i in range(len(vuelos)):
            if vuelos[i][7] == inicio:
                if vuelos[i][8] == fin:
                    pass
            else:
                tkinter.Label(frame, text = "Vuelos no disponibles", bg = "White", font = ("Garamound",12)).place(relx=0.75,rely=0.45, anchor=tkinter.CENTER)
                
            


    #Container principal
    frame = tkinter.Frame(width = 740, height = 500, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
    tkinter.Label(frame, text = "Datos de Vuelo", fg = "#00576C", font = ("Garamound",38), bg = "white").place(relx = 0.28, rely = 0.16, anchor=tkinter.CENTER)

    #Logo--Container principal
    Vuelos = ctk.CTkImage(Image.open(fr"Logos\Vuelos.png"), size = (120,120))
    text = ctk.CTkLabel(master = ventana, image = Vuelos, text = "")
    text.place(relx=0.72,rely=0.26, anchor=tkinter.CENTER)

    #Container secundario
    frame1 = tkinter.Frame(frame, width = 740, height = 332, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame1.place(relx=0.5,rely=0.67, anchor=tkinter.CENTER)

    #Subcontainer secundario, Ida
    ida = tkinter.Frame(frame1, width = 250, height = 38, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#94D513", highlightthickness = 2)
    ida.place(relx=0.2,rely=0.15, anchor=tkinter.CENTER)

    #Datos subcontainer secundario, Ida
    tkinter.Label(ida, text = "Solo ida", bg = "White", font = ("Garamound",12)).place(relx=0.75,rely=0.45, anchor=tkinter.CENTER)
    ida_logo = ctk.CTkImage(Image.open(fr"Logos\ida_logo.png"), size=(19, 19))
    text1 = ctk.CTkLabel(master = ida, image = ida_logo, text = "")
    text1.place(relx=0.55,rely=0.45, anchor=tkinter.CENTER)

    #Subcontainer secundario, Personas
    cant_personas = ctk.CTkEntry(frame1, bg_color = "White", font = ("Garamound",15), width = 150, height = 38, border_color = "#0B99B9")
    cant_personas.place(relx=0.83,rely=0.15, anchor=tkinter.CENTER)
    persona_logo = ctk.CTkImage(Image.open(fr"Logos\perfil.png"), size=(32,32))
    text1 = ctk.CTkLabel(master = frame1, image = persona_logo, text = "")
    text1.place(relx=0.69,rely=0.15, anchor=tkinter.CENTER)

    #Container terciario
    frame2 = tkinter.Frame(frame1, width = 740, height = 233, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame2.place(relx=0.5,rely=0.65, anchor=tkinter.CENTER)

    #Subcontainer terciario, origen
    origen = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), width = 200, height = 42, border_color = "#0B99B9")
    origen.place(relx=0.2,rely=0.28, anchor=tkinter.CENTER)
    tkinter.Label(frame2, text = "Origen", font = ("Garamoun",13), bg = "white", fg = "#00576C").place(relx = 0.16, rely = 0.38)

    #Subcontainer terciario, destino
    destino = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), width = 200, height = 42, border_color = "#0B99B9")
    destino.place(relx=0.5,rely=0.28, anchor=tkinter.CENTER)
    tkinter.Label(frame2, text = "Destino", font = ("Garamoun",13), bg = "white", fg = "#00576C").place(relx = 0.46, rely = 0.38)

    #Subcontainer terciario, fecha
    fecha = ctk.CTkEntry(frame2, bg_color = "White", font = ("Garamound",15), width = 200, height = 42, border_color = "#0B99B9")
    fecha.place(relx=0.8,rely=0.28, anchor=tkinter.CENTER)
    tkinter.Label(frame2, text = "Fecha", font = ("Garamoun",13), bg = "white", fg = "#00576C").place(relx = 0.76, rely = 0.38)

    #Boton buscar
    buscar = ctk.CTkButton(frame2, text = "Buscar", fg_color = "#0B99B9", command = datos_buscar, font = ("Garamond",22), height = 40, width = 130)
    buscar.place(relx=0.5,rely=0.76, anchor=tkinter.CENTER)

    ventana.mainloop()
datos()