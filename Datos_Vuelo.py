import tkinter 
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox

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

    #Vaciar casillas
    def delete_casillas():
        cant_personas.delete(0, tkinter.END)
        origen.delete(0, tkinter.END)
        destino.delete(0, tkinter.END)
        fecha.delete(0, tkinter.END)

    #Pedir infromación completa
    def mensaje_error():
        messagebox.showinfo(message="Por favor, complete los campos", title="Error")

    def datos_buscar():
        #Recolectamos información
        inicio = origen.get()
        fin = destino.get()
        dia = fecha.get()
        fechas_vuelos = []
        precios_vuelos = []
        precios_vuelos1 = []
        hora_vuelos = []
        vuelos = []
        acum = 0
        #Se evalua si los campos se encuentran vacios
        try:
            if inicio == "" or fin == "" or dia == "": #Si los campos estan vacios se genera un error
                raise ValueError
        except ValueError:
            mensaje_error()
        else:
            #Abrir archivo txt
            with open("BD_Vuelos.txt", "r") as archivo:
                usuario = archivo.read()
                usuario = usuario.split("\n")
                for i in range(len(usuario)):
                    vuelo = usuario[i].split(",") 
                    vuelo = [dato.strip().strip("'") for dato in vuelo]
                    vuelos.append(vuelo)
            #Si los datos son negativos genera error
            try:
                people = int(cant_personas.get()) #Verifica que sea entero
                if people <= 0:
                    raise ValueError
            except:
                messagebox.showinfo(message="Cantidad de personas incorrecta", title="Error")
            else:
                #Recorre BD_Vuelos.txt
                for i in range(len(vuelos)):
                    #Verifica fecha, origen y destino para mostrar unicamente los datos del usuario
                    if vuelos[i][1] == dia and vuelos[i][7] == inicio and vuelos[i][8] == fin:
                        hora_vuelos.append(vuelos[i][2:4])
                        precios_vuelos1.append(vuelos[i][4:7])
                    #Verifica información de origen y destino
                    if vuelos[i][7] == inicio:
                        if vuelos[i][8] == fin:
                            #Si es correcta suma acum, agrega fechas y precios
                            acum += 1
                            fechas_vuelos.append(vuelos[i][1])
                            precios_vuelos.append(vuelos[i][4:7])
                    #Si los vuelos no se encuentran genera error
                    else:
                        tkinter.Label(frame, text = "Vuelos no disponibles", fg="red", bg = "White", font = ("Garamound",12)).place(relx=0.5,rely=0.79, anchor=tkinter.CENTER)
                #Si se encuentran vuelos en la BD entra
                if acum >= 1:
                    ventana.destroy()
                    ventana2 = tkinter.Tk() #Crear ventana
                    ventana2.title("Sky-Voyage") #Titulo
                    ventana2.configure(bg = "white")
                    #Centrar la ventana tamaño pc
                    ventana2_width=1000
                    ventana2_height=650
                    ventana2.resizable(0,0)
                    screen_width=ventana2.winfo_screenwidth()
                    screen_height=ventana2.winfo_screenheight()
                    x=(screen_width/2)-(ventana2_width/2)
                    y=(screen_height/2)-(ventana2_height/2)
                    ventana2.geometry(f'{ventana2_width}x{ventana2_height}+{int(x)}+{int(y)}')
                    #Icono superior izquierdo
                    ventana2.iconbitmap("Logos\Avion.ico") 

                    #Tema predeterminado
                    ctk.set_default_color_theme("blue")

                    #Llamar archivo de servicios
                    def paquetes():
                        ida1 = ida.cget("text")
                        first_hora1 = first_hora.cget("text")
                        desde1 = desde.cget("text")
                        llegada1 = llegada.cget("text")
                        second_hora1 = second_hora.cget("text")
                        price_min1 = price_min.cget("text")
                        print(ida1, first_hora1, desde1, llegada1, second_hora1, price_min1)
                        ventana2.destroy()
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

                        frame = tkinter.Frame(ventana, bg = "white", width = 600, height = 50, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
                        frame.place(relx = 0.2, rely = 0.03)

                        tkinter.Label(ventana, bg = "white", text = "Nuestros Servicios", font = ("Berlin Sans FB",23), fg = "#00576C").place(relx=0.5, rely=0.07, anchor=tkinter.CENTER)

                        frame1 = tkinter.Frame(ventana, bg = "white", width = 300, height = 500, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
                        frame1.place(relx = 0.02, rely = 0.16)

                        #Paquete Aluminio
                        tkinter.Label(frame1, text = "Aluminio", font = ("Berlin Sans FB",20), bg = "white").place(relx=0.32, rely=0.03)

                        tkinter.Label(frame1, text = " 1 artículo personal (bolso) \n (Debe caber debajo del asiento)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.12, rely=0.13)
                        tkinter.Label(frame1, text = " 1 equipaje de mano (10 kg) \n (Desde $195.100 COP)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.16, rely=0.25)
                        tkinter.Label(frame1, text = " Equipaje de bodega (23 kg) \n (Desde $175.600 COP)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.17, rely=0.37)
                        tkinter.Label(frame1, text = " Asiento Economy \n (Aleatoria-clasificado Aluminio)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.12, rely=0.49)
                        tkinter.Label(frame1, text = " Cambios de vuelo \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.61)
                        tkinter.Label(frame1, text = " Reembolso \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.74)

                        seleccionar1 = ctk.CTkButton(frame1, text = "Seleccionar", height = 35, font = ("Berlin Sans FB",17))
                        seleccionar1.place(relx = 0.26, rely = 0.88)


                        frame2 = tkinter.Frame(ventana, bg = "white", width = 300, height = 500, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
                        frame2.place(relx = 0.35, rely = 0.16)

                        #Paquete Diamante
                        tkinter.Label(frame2, text = "Diamante", font = ("Berlin Sans FB",20), bg = "white").place(relx=0.31, rely=0.03)

                        tkinter.Label(frame2, text = " 1 artículo personal (bolso) \n (Debe caber debajo del asiento)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.13, rely=0.13)
                        tkinter.Label(frame2, text = " 1 equipaje de bodega (23 kg) (Debe \n caber en el compartimiento superior)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.08, rely=0.25)
                        tkinter.Label(frame2, text = " 1 equipaje de mano (10 kg) \n (Entrega el equipaje en el counter)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.11, rely=0.37)
                        tkinter.Label(frame2, text = " Asiento Economy (Filas específicas \n disponibles de manera aleatoria)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.1, rely=0.49)
                        tkinter.Label(frame2, text = " Cambios de vuelo \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.61)
                        tkinter.Label(frame2, text = " Reembolso \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.74)

                        seleccionar2 = ctk.CTkButton(frame2, text = "Seleccionar", height = 35, font = ("Berlin Sans FB",17))
                        seleccionar2.place(relx = 0.26, rely = 0.88)
                        

                        frame3 = tkinter.Frame(ventana, bg = "white", width = 300, height = 500, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 3)
                        frame3.place(relx = 0.68, rely = 0.16)

                        #Paquete Premium
                        tkinter.Label(frame3, text = "Premium", font = ("Berlin Sans FB",20), bg = "white").place(relx=0.33, rely=0.03)

                        tkinter.Label(frame3, text = " 1 artículo personal (bolso) \n (Debe caber debajo del asiento)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.13, rely=0.13)
                        tkinter.Label(frame3, text = " 1 equipaje de mano (10 kg) (Debe \n caber en el compartimiento superior)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.09, rely=0.25)
                        tkinter.Label(frame3, text = " 1 equipaje de bodega (23 kg) \n (Entrega el equipaje en el counter)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.11, rely=0.37)
                        tkinter.Label(frame3, text = " Asiento Plus (Sujeto \n a disponibilidad-clasificado Premium)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.09, rely=0.49)
                        tkinter.Label(frame3, text = " Cambios de vuelo \n (Sin cargo por cambio, antes del vuelo)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.07, rely=0.61)
                        tkinter.Label(frame3, text = " Reembolso \n (No es permitido)", font = ("Berlin Sans FB",12), bg = "white").place(relx=0.27, rely=0.74)

                        seleccionar3 = ctk.CTkButton(frame3, text = "Seleccionar", height = 35, font = ("Berlin Sans FB",17))
                        seleccionar3.place(relx = 0.27, rely = 0.88)

                        ventana.mainloop()


                    #Destino
                    tkinter.Label(ventana2, text = "Ida: ", fg = "#0B99B9", bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.03, rely = 0.03)
                    #Distancia para Cali
                    if inicio == "Cali":
                        tkinter.Label(ventana2, text = inicio, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.08, rely = 0.03)
                        tkinter.Label(ventana2, text = "a", bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.125, rely = 0.03)
                        tkinter.Label(ventana2, text = fin, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.15, rely = 0.03)
                    #Distancia para Santa Marta
                    elif inicio == "Santa Marta":
                        tkinter.Label(ventana2, text = inicio, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.08, rely = 0.03)
                        tkinter.Label(ventana2, text = "a", bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.22, rely = 0.03)
                        tkinter.Label(ventana2, text = fin, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.24, rely = 0.03)
                    #Distancia para Medellin
                    elif inicio == "Medellin":
                        tkinter.Label(ventana2, text = inicio, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.08, rely = 0.03)
                        tkinter.Label(ventana2, text = "a", bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.175, rely = 0.03)
                        tkinter.Label(ventana2, text = fin, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.2, rely = 0.03)
                    #Distancia para Bogota
                    elif inicio == "Bogota":
                        tkinter.Label(ventana2, text = inicio, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.08, rely = 0.03)
                        tkinter.Label(ventana2, text = "a", bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.17, rely = 0.03)
                        tkinter.Label(ventana2, text = fin, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.2, rely = 0.03)
                    #Distancia para Cartagena
                    elif inicio == "Cartagena":
                        tkinter.Label(ventana2, text = inicio, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.08, rely = 0.03)
                        tkinter.Label(ventana2, text = "a", bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.205, rely = 0.03)
                        tkinter.Label(ventana2, text = fin, bg = "white", font = ("Berlin Sans FB",19)).place(relx = 0.23, rely = 0.03)

                    #Añadir fechas y precios
                    space = 0
                    for k in range(len(fechas_vuelos)):
                                #Muestra automaticamente todas las fechas de los vuelos
                                tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 1, column = 0)
                                tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 2, column = 0)
                                tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 3, column = 0)
                                tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 4, column = 0)
                                frame5 = tkinter.Frame(ventana2, highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
                                frame5.grid(row=5,column=1 +space, padx=4)
                                #Fechas-------Se imprimen todas en posicion K
                                fechas = tkinter.Label(frame5, text = fechas_vuelos[k], width = 10, bg = "white", font = ("Berlin Sans FB",10))
                                fechas.grid(row=5,column=1 +space)
                                space += 1


                    #Texto Ordenar por...
                    tkinter.Label(ventana2, text = "Ordenar por: ", bg = "white", font = ("Berlin Sans FB",17)).place(relx = 0.04, rely = 0.27)
                    #Filtrar por mejor precio
                    best_price = ctk.CTkButton(ventana2, text = "Mejor precio", width = 60, height = 40, font = ("Berlin Sans FB",20))
                    best_price.place(relx=0.24,rely=0.29, anchor=tkinter.CENTER)

                    space = 0
                    for t in range(len(hora_vuelos)):
                        #Muestra automaticamente las horas, origen, destino y precio de los vuelos del usuario
                        tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 5, column = 0)
                        tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 6, column = 0)
                        tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 7, column = 0)
                        tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 8, column = 0)
                        tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 9, column = 0)
                        tkinter.Label(ventana2, text = "Nada", fg = "white", bg = "white").grid(row = 10, column = 0)
                        #Origen--------Se imprimen en bucle
                        ida = tkinter.Label(ventana2, text = inicio.upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12))
                        ida.grid(row=12 +space,column=2, pady= 17)
                        #Hora de salida---------Se imprimen en bucle
                        first_hora = tkinter.Label(ventana2, text = "(" +hora_vuelos[t][0] +")", width = 9, bg = "white", font = ("Berlin Sans FB",12))
                        first_hora.grid(row=12 +space,column=3, pady= 17)
                        #Linea
                        linea = tkinter.Label(ventana2, text = "-----------------------------------------------", width = 9, bg = "white", font = ("Berlin Sans FB",12))
                        linea.grid(row=12 +space,column=4, pady= 17)
                        #Destino---------Se imprimen en bucle
                        llegada = tkinter.Label(ventana2, text = fin.upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12))
                        llegada.grid(row=12 +space,column=5, pady= 17)
                        #Hora de llegada-------Se imprimen en bucle
                        second_hora = tkinter.Label(ventana2, text = "(" +hora_vuelos[t][1] +")", width = 9, bg = "white", font = ("Berlin Sans FB",12))
                        second_hora.grid(row=12 +space,column=6, pady= 17,)
                        #Desde texto
                        desde = tkinter.Label(ventana2, text = "Desde:  ", width = 9, bg = "white", font = ("Berlin Sans FB",12))
                        desde.grid(row=12 +space,column=7, pady= 17)
                        #Precio minimo----------Se imprimen en bucle
                        price_min = tkinter.Label(ventana2, text = "COP. " +precios_vuelos1[t][0], width = 10, bg = "white", font = ("Berlin Sans FB",12))
                        price_min.grid(row=12 +space,column=8, pady= 17)
                        #Boton seleccionar
                        seleccionar = ctk.CTkButton(ventana2, text = "Seleccionar", command = paquetes, width = 20, font = ("Berlin Sans FB",16))
                        seleccionar.grid(row=12 +space,column=10, pady= 17)
                        space += 1
                        

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