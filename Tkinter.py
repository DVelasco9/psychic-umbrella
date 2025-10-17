#IMPORTAR LIBRERIAS
from tkinter import * 

from tkinter import ttk


#CREAR VENTANA
root = Tk() 


frm = ttk.Frame(root, padding=100)

frm.grid()
ttk.Label(frm, text="Hola mundo").grid(column=0, row=0)
ttk.Label(frm, text="EL JAJAS 2").grid(column=4, row=0)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=0)

#LOOP PRINCIPAL
root.mainloop() 
