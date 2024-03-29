from tkinter import *
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import webbrowser
from api_response import lets_try
from threading import Thread
import matplotlib.pyplot as plt

"""
This file has a small change within the plot function 
that adds the ability to add and remove plots when clicking on the button multiple times
"""


class Main():
    root = Tk()
    root.geometry("700x500")
    root.minsize(500, 550)
    root.configure(bg='White')
    root.title("HALT Data")
    graph_label = None

    def __init__(self):
        self.graph_data = {}
        self.api_response = {}

        # configure the column and row sizes
        for i in range(3):
            self.root.columnconfigure(i, weight=1, minsize=0)
        self.root.rowconfigure(0, weight=1, minsize=20)
        self.root.rowconfigure(1, weight=1, minsize=20)
        self.root.rowconfigure(2, weight=2, minsize=20)
        self.root.rowconfigure(3, weight=1, minsize=5)

        # Load the first image into the label and display
        self.create_graph_as_image()

        # Create 3 buttons in the top row
        button = Button(
            text="Jongens", command=lambda: self.plot(-1, "red"), bg="red", width=16, fg="white", font="Helvetica 12 bold")
        button.grid(row=1, column=0)
        button = Button(text="Meiden",
                        command=lambda: self.plot(1, "blue"), bg="blue", width=16, fg="white", font="Helvetica 12 bold")
        button.grid(row=1, column=1)
        button = Button(text="Totaal",
                        command=lambda: self.plot(0, "green"), bg="green", width=16, fg="white", font="Helvetica 12 bold")
        button.grid(row=1, column=2)

        # Create a link to the data
        link_label = Label(text="Data source   ", width=10, bg="white",
                           fg="darkblue", cursor="hand2", underline=0)
        link_label.bind("<Button-1>", lambda e: self.callback(
            "https://data.overheid.nl/dataset/5103-halt-jongeren-van-12-tot-18-jaar--delictgroep--persoonskenmerken#panel-resources"))
        link_label.grid(row=3, column=2, sticky="NE")
        api_retrieval = Thread(target=self.retrieve_coords, daemon=True)
        api_retrieval.start()
        self.plot(-1, "red")

    def plot(self, categorization, color):
        # Delete color from graph dict when button is pressed when color already exists, else create color in dict
        try:
            del self.graph_data[color]
        except KeyError:
            if color in self.api_response:
                self.graph_data[color] = self.api_response[color][0], self.api_response[color][1]
            else:
                x, y = lets_try(categorization)
                self.graph_data[color] = x, y
                self.api_response[color] = x, y
        fig = Figure(figsize=(7, 5), dpi=100)
        plt.style.use('seaborn-v0_8')
        ax = fig.add_subplot(111)
        ax.set_title("Delicten jongeren 12 tot 18 jaar", fontsize=16)
        ax.set_xlabel("Periode", fontsize=12)
        ax.set_ylabel("Totaal delicten", fontsize=12)
        ax.tick_params(axis='x', labelsize=8)
        ax.tick_params(axis='y', labelsize=10)
        fig.autofmt_xdate(rotation=45)
        # For items in colors and data in dict, make their own plot
        for colors in self.graph_data:
            line, = ax.plot(self.graph_data[colors][0], self.graph_data[colors][1], c=colors)
            if colors == 'red':
                line.set_label("Jongens")
                ax.legend()
            if colors == 'blue':
                line.set_label("Meiden")
                ax.legend()
            if colors == 'green':
                line.set_label("Totaal")
                ax.legend()
        ax.set_ybound(0, 25000)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, columnspan=100)

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
        self.graph_label.grid(column=0, row=2, columnspan=100)

    def load_image(self, path="graph.png", size=(500, 500)):
        img = Image.open(path)
        resized_img = img.resize(size)
        return ImageTk.PhotoImage(resized_img)

    def retrieve_coords(self):
        x, y = lets_try(-1)
        self.api_response['red'] = x, y
        x, y = lets_try(0)
        self.api_response['green'] = x, y
        x, y = lets_try(1)
        self.api_response['blue'] = x, y


test = Main()
test.root.mainloop()
