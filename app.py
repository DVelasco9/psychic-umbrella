
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

root = tk.Tk()

#SETTING SOME WINDOW PROPERTIES
root.title("RK EXAMPLE")
root.configure(background="white")
root.minsize(200,200)
root.maxsize(2000,2000)
root.geometry("500x500+500+100")

#CREATE TWO LABELS
label1 = tk.Label(root, text="Halloween is best holiday in the year")
label1.pack()
tk.Label(root, text="...").pack()

#DISPLAY IMAGES
image_path = r"c:\Users\Diego\Downloads\˚₊ᘛart creditᕀ🎐➧ @ AdeptaReality on x.jpg"
original_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(original_image)
tk.Label(root, image=tk_image).pack()

#CREATE AN EXIT BUTTON 
#salida = ttk.Frame(root, padding=10)
#salida.grid()
#ttk.Button(salida, text="salida", command=root.destroy).grid(column=1, row=0)

root.mainloop()