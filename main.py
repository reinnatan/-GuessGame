from functools import partial
import os
from tkinter import Label, StringVar, OptionMenu, Button
from base_form import BaseForm
from quest import QuestPage
from login import LoginPage

class Main(BaseForm):
    def playAction(self):
        self.destroy()
        print(self.clicked.get())
        questPage = QuestPage(self.clicked.get())
        questPage.tkraise()

    def exitAction(self):
        self.destroy()
        loginPage = LoginPage()
        loginPage.tkraise()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        dirlist = os.listdir ("categories")
        
        clicked = StringVar()
        clicked.set(dirlist[0])
        self.clicked = clicked

        #define label
        label = Label(self, text="Categories")
        label.place(x=self.width*0.35, y=self.height*0.25, height=30, width=100)

        #define dropdown menu
        dropdown = OptionMenu(self, clicked, *dirlist)
        dropdown.place(x=self.width*0.35+105, y=self.height*0.25, height=30, width=130)

        #define play button
        playAction = partial(self.playAction)
        buttonMain = Button(self, text="Play", command=playAction)
        buttonMain.place(x=self.width*0.35, y=(self.height*0.25)+35, height=30, width=117*2)
        
        #define exit back to login button
        exitAction = partial(self.exitAction)
        exitMain = Button(self, text="Exit", command=exitAction)
        exitMain.place(x=self.width*0.35, y=(self.height*0.25)+70, height=30, width=117*2)


if __name__ == "__main__":
    loginPage = Main()
    loginPage.mainloop()