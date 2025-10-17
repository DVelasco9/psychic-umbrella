#IMPORTAR LIBRERIAS
from tkinter import * 
from tkinter import ttk


#CREAR VENTANA
root = Tk() 

Label(root, text="Texto").place(x = 1000, y = 50)

# def on_key_press(event):
#     print(f"Key pressed {event.keysym}")
# def on_left_click(event):
#     print(f"Left click at {event.x}, {event.y}")
# def on_right_click(event):
#     print(f"Right click at {event.x}, {event.y}")
# def on_mouse_motion(event):
#     print(f"Mouse moved to {event.x}, {event.y}")

# root.bind("<KeyPress>", on_key_press)
# root.bind("<Button-1>", on_left_click)
# root.bind("<Button-3>", on_right_click)
# root.bind("<Motion>", on_mouse_motion)


#LIST CREATION
#L = Listbox(root)
#L.insert(1, "Option 1")
#L.insert(2, "Option 2")
#L.insert(3, "Option 3")
#L.pack()

#BUTTON CREATION 
#var1= IntVar()
#Radiobutton(root, text="Option 1", variable = var1, value=1).pack()
#Radiobutton(root, text="Option 2", variable = var1, value=2).pack()


#Checkbutton(root, text="option 1", variable=var1).grid(row=0, sticky=N)
#var2 = IntVar()
#Checkbutton(root, text="Option 2", variable=var2).grid(row=0, sticky=E)

#11=Label(root, text="First name").grid(row=0)
#12=Label(root, text="Last name").grid(row=1)
#e1 = Entry(root)
#e2= Entry(root)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#frm = ttk.Frame(root, padding=100)

#frm.grid()
#ttk.Label(frm, text="Hola mundo").grid(column=0, row=0)
#ttk.Label(frm, text="EL JAJAS 2").grid(column=2, row=0)

#EXIT BUTTON
#ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=0)

#LOOP PRINCIPAL
root.mainloop() 
