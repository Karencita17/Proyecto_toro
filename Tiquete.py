import tkinter as tk

def ticket():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Sky-Voyage") #Titulo
    #Centrar la ventana tamaño pc
    root_width=1000
    root_height=650
    root.resizable(0,0)
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x=(screen_width/2)-(root_width/2)
    y=(screen_height/2)-(root_height/2)
    root.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')

    #Icono superior izquierdo
    root.iconbitmap("Logos/Avion.ico")

    # Configurar el tamaño de la ventana
    root.geometry("650x280")

    # Crear el marco azul claro para el título superior
    frame_titulo_superior = tk.Frame(root, bg="light blue", width=600, height=50)
    frame_titulo_superior.pack(side="top", fill="x")

    # Crear el texto del título superior en el marco azul claro
    titulo_superior = tk.Label(frame_titulo_superior, text="Pase de abordaje", bg="light blue", fg="white", font=("Garamound", 16))
    titulo_superior.pack()

    # Crear el marco azul para el título
    frame_titulo = tk.Canvas(root, bg="blue", width=150, height=250)
    frame_titulo.pack(side="left", fill="y")

    # Crear el texto del título en el marco azul
    titulo = frame_titulo.create_text(80,120, text="Pase de abordaje", angle=90, fill="white", font=("Garamound", 19))

    # Crear el marco blanco para los detalles del pase
    frame_detalles = tk.Frame(root, bg="white", width=400, height=250)
    frame_detalles.pack(side="right", fill="both", expand=True)

    # Crear y agregar las etiquetas de los detalles del pase
    nombre_pasajero = tk.Label(frame_detalles, text="Nombre Pasajero", bg="white", font=("Arial", 10)).place(relx=0.20,rely=0.1, anchor=tk.CENTER)
    # pasajero = tk.Label(frame_detalles, text="Alejandro Sierra", bg="white", font=("Arial", 12)).place(relx=0.20,rely=0.2, anchor=tk.CENTER)
    origen_vuelo_fecha = tk.Label(frame_detalles, text="Origen                                Vuelo                 Fecha", bg="white", font=("Arial", 10)).place(relx=0.4,rely=0.35, anchor=tk.CENTER)
    # ciudad = tk.Label(frame_detalles, text="BOG", bg="white", font=("Arial", 11)).place(relx=0.13,rely=0.45, anchor=tk.CENTER)
    # vuelo = tk.Label(frame_detalles, text="BOG", bg="white", font=("Arial", 11)).place(relx=0.46,rely=0.45, anchor=tk.CENTER)
    # fecha = tk.Label(frame_detalles, text="BOG", bg="white", font=("Arial", 11)).place(relx=0.66,rely=0.45, anchor=tk.CENTER)
    destino_hora = tk.Label(frame_detalles, text="Destino                                                        Hora", bg="white", font=("Arial", 10)).place(relx=0.39,rely=0.6, anchor=tk.CENTER)
    # destino = tk.Label(frame_detalles, text="CAR", bg="white", font=("Arial", 12)).place(relx=0.13,rely=0.7, anchor=tk.CENTER)
    # hora = tk.Label(frame_detalles, text="CAR", bg="white", font=("Arial", 12)).place(relx=0.66,rely=0.7, anchor=tk.CENTER)


    with open("BD_Usuarios1.txt", "r") as archivo: 
        info_vuelos = archivo.readlines()
    #Se toma la ultima fila
    ultimo = info_vuelos[-1]
    ultimo = ultimo.split(",") #Se omiten ,
    for i in range(len(ultimo)):

        tk.Label(frame_detalles, text = ultimo[0].upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.13,rely=0.45, anchor=tk.CENTER)
             
        tk.Label(frame_detalles, text = "(" +ultimo[3] +")", width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.66,rely=0.7, anchor=tk.CENTER)
                 
        tk.Label(frame_detalles, text = ultimo[1].upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.15,rely=0.7, anchor=tk.CENTER)
                         
        tk.Label(frame_detalles, text = ultimo[2].upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.70,rely=0.45, anchor=tk.CENTER)

        tk.Label(frame_detalles, text = ultimo[17].upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.46,rely=0.45, anchor=tk.CENTER)

        tk.Label(frame_detalles, text = ultimo[9].upper(), width = 9, bg = "white", font = ("Berlin Sans FB",12)).place(relx=0.20,rely=0.2, anchor=tk.CENTER)


    # Iniciar el bucle principal de Tkinter
    root.mainloop()
