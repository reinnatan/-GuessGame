from functools import partial
import tkinter as tk
from tkinter import Button, Entry, Label, StringVar
from base_form import BaseForm
from PIL import Image, ImageTk

class LoginPage(BaseForm):
    def validateLogin(self, username, password):
        if (username.get()=="test" and password.get()=="test"):
            self.destroy()
            from main import Main
            main = Main()
            main.tkraise()
        #print("username entered :", username.get())
        #print("password entered :", password.get())

    def gotoRegister(self):
        print("register called")
        loginPage.destroy()
        from register import RegisterPage
        registerPage = RegisterPage()
        registerPage.tkraise()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        #define title 
        titleLabel = Label(self, text="Login Page")
        titleLabel.place(x=self.width*0.3, y=self.height*0.23, width=(150*2)+5, height=30)        

        #define username
        usernameLabel = Label(self, text="User Name")
        usernameLabel.place(x=self.width*0.3, y=self.height*0.3, width=150, height=30)        
        username = StringVar()
        usernameEntry = Entry(self, textvariable=username)
        usernameEntry.place(x=(self.width*0.3)+155, y=self.height*0.3, width=150, height=30)

        #define password
        passwordLabel = Label(self, text="Password")
        passwordLabel.place(x=self.width*0.3, y=(self.height*0.3)+35, width=150, height=30)
        password = StringVar()
        passwordEntry = Entry(self, textvariable=password, show='*')
        passwordEntry.place(x=(self.width*0.3)+155, y=(self.height*0.3)+35, width=150, height=30)

        #define sign in button
        validateLogin = partial(self.validateLogin, username, password)
        loginButton = Button(self, text="Sign in", command=validateLogin)
        loginButton.place(x=(self.width*0.3), y=(self.height*0.3)+70, width=150, height=30)

        #define register 
        gotogister = partial(self.gotoRegister)
        gotogister = Button(self, text="Sign up", command=gotogister)
        gotogister.place(x=(self.width*0.3)+155, y=(self.height*0.3)+70, width=150, height=30)

        

if __name__ == "__main__":
    global loginPage
    loginPage = LoginPage()
    loginPage.mainloop()