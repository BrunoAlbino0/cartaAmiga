from tkinter import Frame, Label, Button,PhotoImage,Entry
#Para fazer a importação https://blog.finxter.com/how-to-install-pillow-on-pycharm/
from PIL import Image, ImageTk

class LoginPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        background_color = "#f6a2a6"
        main_tittle_color = "#ffffff"
        input_color = "#f2d0cb"
        labels_font = ("Radley", 12, "bold")

        self.configure(bg=background_color)

        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41, "bold"), bg=background_color, fg=main_tittle_color)
        self.label_titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=2, padx=10, pady=10)

        #New User
        self.label_new_user = Label(self, text="New User: Registrate ", font=("Radley", 25, "bold"), bg=background_color)
        self.label_new_user.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        self.label_nickname_unregisted = Label(self, text="Nick name:", bg=background_color, font=labels_font)
        self.Input_nickname_unregisted = Entry(self, bg=input_color)
        self.label_nickname_unregisted.grid(row=2, column=0, padx=10, sticky="w")
        self.Input_nickname_unregisted.grid(row=2, column=0, padx=(110, 20), sticky="we")

        self.label_password_unregisted = Label(self, text="Password:", bg=background_color, font=labels_font)
        self.Input_password_unregisted = Entry(self, show="*", bg=input_color)
        self.label_password_unregisted.grid(row=3, column=0, padx=10, sticky="w")
        self.Input_password_unregisted.grid(row=3, column=0, padx=(110, 20), sticky="we")

        self.btn_Regist_New_User = Button(self, text="Regist")
        self.btn_Regist_New_User.grid(row=2, column=2, padx=10, pady=10, rowspan=2)

        #Registraded user
        self.label_registed_user = Label(self, text="Registrated User:Login ", font=("Radley", 25, "bold"), bg=background_color)
        self.label_registed_user.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        self.label_nickname_registed = Label(self, text="Nick name:", bg=background_color, font=labels_font)
        self.Input_nickname_registed = Entry(self, bg=input_color)
        self.label_nickname_registed.grid(row=5, column=0, padx=10, sticky="w")
        self.Input_nickname_registed.grid(row=5, column=0, padx=(110, 20), sticky="we")

        self.label_password_registed = Label(self, text="Password:", bg=background_color, font=labels_font)
        self.Input_password_registed = Entry(self, show="*", bg=input_color)
        self.label_password_registed.grid(row=6, column=0, padx=10, sticky="w")
        self.Input_password_registed.grid(row=6, column=0, padx=(110, 20), sticky="we")

        self.btn_Login = Button(self, text="Login")

        self.btn_Login.grid(row=5, column=2, padx=10, pady=10, rowspan=2)

        self.btn_list_all_users = Button(self, text="List all users")
        self.btn_list_all_users.grid(row=8, column=2, padx=10, pady=10, rowspan=2)
