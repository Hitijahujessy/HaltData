from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("600x600")

canvas = Canvas(background="red")
canvas.grid(column=0, row=1, columnspan=10)

img = Image.open("graph.png")
resized_img = img.resize((500,500), Image.ANTIALIAS)
test = ImageTk.PhotoImage(resized_img)

label = Label(image=test)
label.grid(column=0, row=1, columnspan=100)

for i in range(3):
    root.columnconfigure(i, weight=1, minsize=5)
    
root.rowconfigure(1, weight=2, minsize=5)
root.rowconfigure(0, weight=1, minsize=20)

for j in range(0, 3):
    button = Button(text=f"graph {j}")
    button.grid(row=0, column=j)
        


root.mainloop()
