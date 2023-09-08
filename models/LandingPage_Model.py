from .base import ObservableModel

class LandingPageModel(ObservableModel):
    def __init__(self):
        super().__init__()

    def advance(self, user):
        self.trigger_event("landingPage_advance")

    def exit(self):
        self.trigger_event("LandingPage_exit")