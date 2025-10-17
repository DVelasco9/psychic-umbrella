
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

root = tk.Tk()
root.title("Image Editor")
root.config(bg="skyblue")

#CREATE A FRAME WIDGET
frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)

#CREATING NESTED FRAMES
nested_frame = tk.Frame(frame, width=190, height=190)


#DISPLAY IMAGES
#MYERS: c:\Users\Diego\Downloads\Enid.png
#PSY: c:\Users\Diego\Downloads\˚₊ᘛart-creditᕀ_➧-_-AdeptaReality-on-x.png
pic = tk.PhotoImage(file=r"c:\Users\Diego\Downloads\Enid.png")


#image_path = r"c:\Users\Diego\Downloads\˚₊ᘛart creditᕀ🎐➧ @ AdeptaReality on x.jpg"
#original_image = Image.open(image_path)
#tk_image = ImageTk.PhotoImage(original_image)

#TOOLS FRAME
tools_frame = tk.Frame(root, width=200, height=400, bg="skyblue")
tools_frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)

tk.Label(
    tools_frame,
    text="original image",
    bg = "skyblue",
).pack(padx=5, pady=5)
thumbnail_image = pic.subsample(5,5)
tk.Label(tools_frame, image=thumbnail_image).pack(padx=5, pady=5)


root.mainloop()