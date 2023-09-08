from tkinter import Frame, Label, Button,PhotoImage,Entry
#Para fazer a importação https://blog.finxter.com/how-to-install-pillow-on-pycharm/
from PIL import Image, ImageTk

class LoginPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41))
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=1, padx=10, pady=10)

        #New User
        self.label_new_user = Label(self, text="New User: Registrate ", font=("Radley", 12))
        self.label_new_user.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.label_nickname_unregisted = Label(self, text="nick name")
        self.Input_nickname_unregisted = Entry(self)
        self.label_nickname_unregisted.grid(row=2, column=0, padx=10, sticky="w")
        self.Input_nickname_unregisted.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.label_password_unregisted = Label(self, text="Password")
        self.Input_password_unregisted = Entry(self, show="*")
        self.label_password_unregisted.grid(row=3, column=0, padx=10, sticky="w")
        self.Input_password_unregisted.grid(row=3, column=1, padx=(0, 20), sticky="ew")

        self.btn_Regist_New_User = Button(self, text="Registar")
        self.btn_Regist_New_User.grid(row=2, column=2, padx=10, pady=10, rowspan=2)

        #Registraded user
        self.label_registed_user = Label(self, text="Registrate User:Login ", font=("Radley", 12))
        self.label_registed_user.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.label_nickname_registed = Label(self, text="nick name")
        self.Input_nickname_registed = Entry(self)
        self.label_nickname_registed.grid(row=5, column=0, padx=10, sticky="w")
        self.Input_nickname_registed.grid(row=5, column=1, padx=(0, 20), sticky="ew")

        self.label_password_registed = Label(self, text="Password")
        self.Input_password_registed = Entry(self, show="*")
        self.label_password_registed.grid(row=6, column=0, padx=10, sticky="w")
        self.Input_password_registed.grid(row=6, column=1, padx=(0, 20), sticky="ew")

        self.btn_Login = Button(self, text="Login")
        self.btn_Login.grid(row=5, column=2, padx=10, pady=10, rowspan=2)
