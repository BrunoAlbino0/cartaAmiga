class WelcomePage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Welcome! Click to enter", font=("Radley", 41))