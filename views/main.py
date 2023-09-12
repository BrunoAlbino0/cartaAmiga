from tkinter import Frame, Label, Button
from .root import Root
from .landing_page import LandingPage
from .login_page import LoginPage
from .welcome_page import WelcomePage
from .letter_page import LetterPage
from .select_letter_page import SelectLetterPage
from .menu_page import MenuPage


# restantes janelas

class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}
        self._add_frame(LoginPage, "loginPage")
        self._add_frame(WelcomePage, "welcomePage")
        self._add_frame(MenuPage, "menuPage")
        self._add_frame(SelectLetterPage, "selectLetterPage")
        self._add_frame(LetterPage, "letterPage")
        self._add_frame(LandingPage, "landingPage")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()

    def stop_mainloop(self):
        self.root.destroy()