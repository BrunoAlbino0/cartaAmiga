from Models.model import Model
from views.main import View
class LadingPageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["landingPage"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_Advance.config(command=self.click_on_advance)

    def click_on_advance(self):
        print("Avançar")
        self.view.switch("loginPage")