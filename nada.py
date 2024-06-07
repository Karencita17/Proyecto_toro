import tkinter

ventana = tkinter.Tk()

lista = ["Hola","Adios","SI","NO"]
space = 0
for i in range(len(lista)):
    space += 2
    hola = tkinter.Label(ventana, text = lista[i], fg = "black", bg = "white", font = ("Berlin Sans FB",19))
    hola.grid(row = 1, column = 1 +space)

ventana.mainloop()