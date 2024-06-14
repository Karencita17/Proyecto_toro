import customtkinter as ctk
from tkinter import StringVar, messagebox
import tkinter
import Tiquete
from PIL import Image, ImageTk

def pagar():
    # Crear la ventana principal
    ventana = tkinter.Tk()
    ventana.configure(bg="white")
    ventana.title("Sky-Voyage") #Titulo
    fondo = ctk.CTkImage(Image.open(fr"Logos\fondo.png"), size=(1573, 795))
    text3 = ctk.CTkLabel(master=ventana, image=fondo, text="")
    text3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    # Centrar la ventana tamaño pc
    ventana_width = 1000
    ventana_height = 650
    ventana.resizable(0, 0)
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width / 2) - (ventana_width / 2)
    y = (screen_height / 2) - (ventana_height / 2)
    ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')
    #Icono superior izquierdo
    ventana.iconbitmap("Logos\Avion.ico")

    
    # Crear ventana
    frame = tkinter.Frame(ventana, width = 600, height = 450, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame.place(relx=0.19, rely=0.13)  

    # Título de la ventana
    title_label = tkinter.Label(frame, text="Datos de la Tarjeta", fg = "#00576C", font = ("Garamound",25), bg = "white")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    frame1 = tkinter.Frame(ventana, width = 600, height = 380, bg = "white", highlightbackground = "#0B99B9", highlightcolor = "#0B99B9", highlightthickness = 2)
    frame1.place(relx=0.19, rely=0.26)  

    # Label para Nombre de Titular
    name_label = tkinter.Label(frame1, text="Nombre de Titular:", fg = "#006D87", font = ("Garamound",14), bg = "white")
    name_label.place(relx=0.03, rely=0.05)

    #Icono nombre-Titular
    name_icon = ctk.CTkImage(Image.open(fr"Logos\usuario.png"), size=(25, 25))
    text3 = ctk.CTkLabel(master=frame1, image=name_icon, text="")
    text3.place(relx=0.12, rely=0.21, anchor=tkinter.CENTER)

    # Entry para Nombre de Titular
    name_entry = ctk.CTkEntry(frame1, width=400, border_color = "#0B99B9", height = 40)
    name_entry.place(relx=0.18, rely=0.16)

    # Label para Número de la Tarjeta
    card_number_label = tkinter.Label(frame1, text="Número de la Tarjeta:", fg = "#006D87", font = ("Garamound",14), bg = "white")
    card_number_label.place(relx=0.03, rely=0.32)

    #Icono num-tarjeta
    name_icon = ctk.CTkImage(Image.open(fr"Logos\tarjeta-de-credito.png"), size=(35, 35))
    text3 = ctk.CTkLabel(master=frame1, image=name_icon, text="")
    text3.place(relx=0.12, rely=0.48, anchor=tkinter.CENTER)

    # Entry para Número de la Tarjeta
    card_number_entry = ctk.CTkEntry(frame1, width=400, border_color = "#0B99B9", height = 40)
    card_number_entry.place(relx=0.18, rely=0.43)

    # Subtítulo para Fecha de Expiración
    expiration_label = tkinter.Label(frame1, text="Fecha de Expiración:", fg = "#006D87", font = ("Garamound",14), bg = "white")
    expiration_label.place(relx=0.03, rely=0.66)

    # Opciones para Mes y Año
    month_combobox = ctk.CTkComboBox(frame1, values=[f"{i:02d}" for i in range(1, 13)], width=70, height = 35)
    month_combobox.place(relx=0.35, rely=0.65)

    year_combobox = ctk.CTkComboBox(frame1, values=[str(i) for i in range(2024, 2035)], width=80, height = 35)
    year_combobox.place(relx=0.5, rely=0.65)

    # Entry para CVV
    cvv_label = tkinter.Label(frame1, text="CVV:", fg = "#006D87", font = ("Garamound",14), bg = "white")
    cvv_label.place(relx=0.67, rely=0.66)
    cvv_entry = ctk.CTkEntry(frame1, width=80, border_color = "#0B99B9", height = 40)
    cvv_entry.place(relx=0.78, rely=0.65)
                        
    def validate():
        card_number = card_number_entry.get()
        cvv = cvv_entry.get()

        if not card_number.isdigit() or len(card_number) != 16:
            messagebox.showerror("Datos incorrectos.", "Por favor, verifique e intente de nuevo.")
        elif not cvv.isdigit() or len(cvv) != 3:
            messagebox.showerror("Datos incorrectos.", "Por favor, verifique e intente de nuevo.")
        else:
            ventana.destroy()
            Tiquete.ticket()

    accept_button = ctk.CTkButton(frame1, text = "Aceptar", fg_color = "#0B99B9", font = ("Garamond",22), height = 40, width = 130, command=validate) 
    accept_button.place(relx=0.5, rely=0.9, anchor="center")
    
    ventana.mainloop()