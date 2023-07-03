from tkinter import *
from PIL import Image, ImageTk
import webbrowser


class Main():

    root = Tk()
    root.geometry("600x600")
    root.minsize(500, 550)
    root.configure(bg='lightgrey')
    root.title("HALT Data")
    graph_label = None

    def __init__(self):
        
        # configure the column and row sizes
        for i in range(3):
            self.root.columnconfigure(i, weight=1, minsize=5)
        self.root.rowconfigure(1, weight=2, minsize=20)
        self.root.rowconfigure(0, weight=1, minsize=20)
        self.root.rowconfigure(2, weight=1, minsize=5)

        # add an invisible Canvas so the size of the app is fixed
        self.canvas = Canvas(background="lightgrey", width=500, height=500)
        self.canvas.grid(column=0, row=1, columnspan=10)

        # Load the first image into the label and display
        self.create_graph()

        # Create 3 buttons in the top row
        button = Button(text="man graph", command=lambda: self.create_graph(1))
        button.grid(row=0, column=0)
        button = Button(text="woman graph",
                        command=lambda: self.create_graph(2))
        button.grid(row=0, column=1)
        button = Button(text="woman-man graph",
                        command=lambda: self.create_graph(3))
        button.grid(row=0, column=2)
        
        # Create a link to the data
        link_label = Label(text="Data source    ", bg="lightgrey", fg="darkblue", cursor="hand2", underline=0)
        link_label.bind("<Button-1>", lambda e: self.callback("https://data.overheid.nl/dataset/5103-halt-jongeren-van-12-tot-18-jaar--delictgroep--persoonskenmerken#panel-resources"))
        link_label.grid(row=2, column=3)

    def callback(self, url):
        #Opens the url in standard browser
        webbrowser.open_new(url)
    
    def create_graph(self, button=0):
        if self.graph_label:
            # Destroy the previous label
            self.graph_label.destroy()
        img = self.load_image(path=f"graph{button}.png", size=(500, 500))
        self.graph_label = Label(image=img)
        self.graph_label.image = img # for some reason it requires you to define image twice?????????
        self.graph_label.grid(column=0, row=1, columnspan=100)

    def load_image(self, path="graph.png", size=(500, 500)):
        img = Image.open(path)
        resized_img = img.resize(size)
        return ImageTk.PhotoImage(resized_img)


test = Main()
test.root.mainloop()
