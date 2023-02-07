
from View.SignupScreen.signup_screen import SignupScreenView


class SignupScreenController:
    """
    The `SignupScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.signup_screen.SignupScreenModel
        self.view = SignupScreenView(controller=self, model=self.model)

    def get_view(self) -> SignupScreenView:
        return self.view
