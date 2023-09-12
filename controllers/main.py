from .landingPageController import LadingPageController
from .loginPageController import LoginPageController
from .welcomePageController import WelcomePageController
from .menuPageController import MenuPageController
from .selectLetterPageContoller import SelectLetterPageController
from .letterPageController import LetterPageController

from Models.Model import Model
from views.main import View

class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.loginPage_Controller = LoginPageController(model, view)
        self.welcomePage_Controller = WelcomePageController(model, view)
        self.menuPage_Controller = MenuPageController(model, view)
        self.letterPage_Controller = LetterPageController(model, view)
        self.selectLetterPage_Controller = SelectLetterPageController(model, view)
        self.ladingPage_Controller = LadingPageController(model, view)

    def start(self):
        self.view.start_mainloop()

