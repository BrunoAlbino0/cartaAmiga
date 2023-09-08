from .landingPageController import LadingPageController
from models.main import Model
from views.main import View

class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.ladingPage_Controller = LadingPageController(model, view)

    def start(self):
        self.view.start_mainloop()

    def exit(self):
        self.view.stop_mainloop()