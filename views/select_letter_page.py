from tkinter import Frame, Label, Button,PhotoImage,Entry, ttk

class SelectLetterPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        background_color = "#f6a2a6"
        main_tittle_color = "#ffffff"
        self.configure(bg=background_color)

        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41, "bold"), bg=background_color, fg=main_tittle_color)
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=1, padx=10, pady=10)

        self.label_New_Letters = Label(self, text="New Letters", font=("Radley", 20, "bold"), bg=background_color)
        self.label_New_Letters.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.btn_Refresh = Button(self, text="Refresh")
        self.btn_Refresh.grid(row=1, column=1, padx=10, pady=10)

        #columns = ('ID', 'Title', 'Date', 'Sender', 'Select')
        columns = ('ID', 'Title', 'Sender')

        self.tree_letters = ttk.Treeview(self, columns=columns, show='headings')


        # define headings
        self.tree_letters.heading('ID', text='ID')
        self.tree_letters.heading('Title', text='Title')
        #self.tree_letters.heading('Date', text='Date')
        self.tree_letters.heading('Sender', text='Sender')
        #self.tree_letters.heading('Select', text='Select')

        self.tree_letters.grid(row=2, column=0, padx=10, pady=10)

        self.btn_select_letter = Button(self, text="Select")
        self.btn_select_letter.grid(row=2, column=1, padx=10, pady=10)

        self.btn_return = Button(self, text="Return")
        self.btn_return.grid(row=3, column=1, padx=10, pady=10)