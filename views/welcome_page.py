from tkinter import Frame, Label, Button,PhotoImage,Entry

class WelcomePage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        background_color = "#f6a2a6"
        main_tittle_color = "#ffffff"
        self.configure(bg=background_color)


        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41, "bold"), bg=background_color, fg=main_tittle_color )
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=1, padx=10, pady=10)

        self.welcome_label = Label(self, text="Welcome! Click to enter", font=("Radley", 41, "bold"), bg=background_color)
        self.welcome_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.btn_Welcome = Button(self, text="welcome")
        self.btn_Welcome.grid(row=2, column=0, padx=10, pady=10, sticky="ew")