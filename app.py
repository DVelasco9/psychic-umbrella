
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

root = tk.Tk()
root.title("Frame demo")
root.config(bg="skyblue")

#CREATE A FRAME WIDGET
frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)

#DISPLAY IMAGES
#image_path = r"c:\Users\Diego\Downloads\˚₊ᘛart creditᕀ🎐➧ @ AdeptaReality on x.jpg"
#original_image = Image.open(image_path)
#tk_image = ImageTk.PhotoImage(original_image)
#tk.Label(root, image=tk_image).pack()

root.mainloop()