import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Button, Entry, Label, StringVar


class BaseForm(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        ico = Image.open('background/guess.ico')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        width = 700
        height = 500

        self.width = width
        self.height = height
        self.resizable(False, False)
        geometry_str = "%sx%s"%(str(width),str(height))
        self.wm_geometry(geometry_str)
        self.wm_title("Guest Game")
        self.eval('tk::PlaceWindow . center')
        
        # Load and set the background image
        background = Label(self)
        background.place(x=0, y=0, width=700, height=500)
        image = Image.open("background/QuizBackground.png")
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized_image)
        background.configure(image=tk_image)
        background.image = tk_image
