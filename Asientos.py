import tkinter as tk
import customtkinter
import Resumen_compra

def abrir_ventana_seleccion_asientos():
    ventana = tk.Tk() #Crear ventana
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
    customtkinter.set_default_color_theme("blue")

    def resumen_de_la_compra():
        ventana.destroy()
        Resumen_compra.resumen_de_la_compra()

    # Título de la selección de asientos
    lbl_seleccion_asientos = tk.Label(ventana, text="Selección de Asientos", bg = "White", fg = "#0B99B9", font = ("Garamond",30))
    lbl_seleccion_asientos.place(relx=0.46,rely=0.1, anchor=tk.CENTER)

    # Crear el marco para el asiento y las etiquetas de clase
    marco_wrapper = tk.Frame(ventana)
    marco_wrapper.place(relx=0.45,rely=0.50, anchor=tk.CENTER)

    marco_asientos = tk.Frame(marco_wrapper)
    marco_asientos.pack(side="left")


    # Crear etiquetas para las columnas
    columnas = ["A", "B", "C", "D", "E", "F"]
    for i, columna in enumerate(columnas):
        lbl = tk.Label(marco_asientos, text=columna)
        lbl.grid(row=0, column=i+1)

    # Crear los botones para los asientos (72 asientos, 12 filas x 6 columnas)
    num_filas = 12
    num_columnas = 6
    botones_asientos = [[None for _ in range(num_columnas)] for _ in range(num_filas)]

    def seleccionar_asiento(fila, columna):
        asiento = columnas[columna] +"-" +str((fila + 1))
        with open(fr"BD_Usuarios1.txt", 'a') as file:
            mensaje = ""
            mensaje += str(asiento) 
            file.write(mensaje)

    def resumen():
        ventana.destroy()
        Resumen_compra.resumen_de_la_compra()

    for r in range(num_filas):
        lbl = tk.Label(marco_asientos, text=str(r+1))
        lbl.grid(row=r+1, column=0)
        for c in range(num_columnas):
            clase = "Aluminio" if r >= 8 else "Diamante" if r >= 4 else "Premium"
            color = "#0092B5" if clase == "Premium" else "#00B8E5" if clase == "Diamante" else "#FFFFFF"
            btn = tk.Button(marco_asientos, bg=color, width=2, height=1, state="normal" if clase == "Premium" else "disabled", command=lambda r=r, c=c: seleccionar_asiento(r, c))
            btn.grid(row=r+1, column=c+1, padx=2, pady=2)
            botones_asientos[r][c] = btn

    # Crear las etiquetas para las clases
    lbl_premium = tk.Label(ventana, text="Premium", bg="#0092B5", fg="white", width=12, height = 1, font = ("Garamond",15))
    lbl_premium.place(relx=0.65,rely=0.33, anchor=tk.CENTER)
    
    lbl_diamante = tk.Label(ventana, text="Diamante", bg="#00B8E5", fg="white", width=12, height = 1, font = ("Garamond",15))
    lbl_diamante.place(relx=0.65,rely=0.52, anchor=tk.CENTER)

    lbl_aluminio = tk.Label(ventana, text="Aluminio", bg="#CCCCCC", fg="white", width=12, height = 1, font = ("Garamond",15))
    lbl_aluminio.place(relx=0.65,rely=0.68, anchor=tk.CENTER)

    # Botón de selección
    btn_continuar = customtkinter.CTkButton(ventana, text="Continuar", font = ("Garamond",22), height = 35, command = resumen)
    btn_continuar.place(relx=0.85,rely=0.85, anchor=tk.CENTER)

    ventana.mainloop()
