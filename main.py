from tkinter import *
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import webbrowser
from api_response import lets_try


class Main():

    root = Tk()
    root.geometry("800x600")
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

        # Load the first image into the label and display
        self.create_graph_as_image()

        # Create 3 buttons in the top row
        button = Button(
            text="men", command=lambda: self.plot(lets_try(-1), "red"))
        button.grid(row=0, column=0)
        button = Button(text="women",
                        command=lambda: self.plot(lets_try(1), "blue"))
        button.grid(row=0, column=1)
        button = Button(text="total",
                        command=lambda: self.plot(lets_try(0), "green"))
        button.grid(row=0, column=2)

        # Create a link to the data
        link_label = Label(text="Data source    ", bg="lightgrey",
                           fg="darkblue", cursor="hand2", underline=0)
        link_label.bind("<Button-1>", lambda e: self.callback(
            "https://data.overheid.nl/dataset/5103-halt-jongeren-van-12-tot-18-jaar--delictgroep--persoonskenmerken#panel-resources"))
        link_label.grid(row=2, column=3)

        x, y = lets_try(-1)
        self.plot([x, y], "red")

    def plot(self, coords, color):
        fig = Figure(figsize=(7, 5), dpi=100)

        x, y = coords
        ax = fig.add_subplot(111)
        ax.set_title("Delicten jongeren 12 tot 18 jaar", fontsize=12)
        ax.set_xlabel("Periode", fontsize=8)
        ax.set_ylabel("Totaal delicten", fontsize=8)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=12)
        ax.plot(x, y, c=color)
        ax.set_ybound(0, 25000)
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=100)

    def callback(self, url):
        # Opens the url in standard browser
        webbrowser.open_new(url)

    def create_graph_as_image(self, button=0):
        if self.graph_label:
            # Destroy the previous label
            self.graph_label.destroy()
        img = self.load_image(path=f"graph{button}.png", size=(400, 400))
        self.graph_label = Label(image=img)
        # for some reason it requires you to define image twice?????????
        self.graph_label.image = img
        self.graph_label.grid(column=0, row=1, columnspan=100)

    def load_image(self, path="graph.png", size=(500, 500)):
        img = Image.open(path)
        resized_img = img.resize(size)
        return ImageTk.PhotoImage(resized_img)


test = Main()
test.root.mainloop()
