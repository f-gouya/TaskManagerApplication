from PresentationLayer.window import Windows
from PresentationLayer.login import LoginFrame


# from PresentationLayer.register import RegisterFrame
# from PresentationLayer.home import HomeFrame
# from PresentationLayer.profile import ProfileFrame
# from PresentationLayer.user_management import UserManagementFrame
# from PresentationLayer.reset_password import ResetPasswordFrame
# from PresentationLayer.user_request import UserRequestFrame


class MainView:
    def __init__(self):
        self.window = Windows()

        self.frames = {}

        # self.add_frame("user_request", UserRequestFrame(self.window, self))
        # self.add_frame("reset_password", ResetPasswordFrame(self.window, self))
        # self.add_frame("profile", ProfileFrame(self.window, self))
        # self.add_frame("user_management", UserManagementFrame(self.window, self))
        # self.add_frame("home", HomeFrame(self.window, self))
        # self.add_frame("register", RegisterFrame(self.window, self))
        self.add_frame("login", LoginFrame(self.window, self))

        self.window.show_form()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        return frame
