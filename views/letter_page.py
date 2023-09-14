from tkinter import Frame, Label, Button,PhotoImage,Entry, Text, END

class LetterPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        background_color = "#f6a2a6"
        main_tittle_color = "#ffffff"
        input_color = "#f2d0cb"
        self.configure(bg=background_color)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=10)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41, "bold"), bg=background_color, fg=main_tittle_color)
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=1, padx=10, pady=10)

        self.label_letter_tittle = Label(self, text="Tittle:", bg=background_color)
        self.Input_letter_tittle = Text(self, font=("Calibri", 12, "bold"), bg=input_color)
        self.label_letter_tittle.grid(row=1, column=0, padx=10, sticky="w")
        self.Input_letter_tittle.grid(row=2, column=0, padx=(20, 20), sticky="nsew")

        self.label_letter_tittle = Label(self, text="Content", bg=background_color)
        self.label_letter_tittle.grid(row=3, column=0, padx=10, sticky="w")
        self.Input_letter_content = Text(self, font=("Calibri", 12, "bold"), bg=input_color)
        self.Input_letter_content.grid(row=4, padx=(20, 20), sticky="nsew")

        self.btn_go_back = Button(self, text="Return")
        self.btn_go_back.grid(row=5, column=0, padx=10, pady=10)

        self.btn_save_letter = Button(self, text="Save")
        self.btn_save_letter.grid(row=5, column=1, padx=10, pady=10)

        self.btn_show_letter = Button(self, text="Show Selected_Letter")
        self.btn_show_letter.grid(row=6, column=0, padx=10, pady=10)

