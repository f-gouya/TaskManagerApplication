from PresentationLayer.window import Windows
from PresentationLayer.login import LoginFrame
from PresentationLayer.home import HomeFrame
from PresentationLayer.admin_manage_form import AdminManageFrame


class MainView:
    def __init__(self):
        self.window = Windows()

        self.frames = {}
        self.add_frame("admin_manage", AdminManageFrame(self.window, self))
        self.add_frame("home", HomeFrame(self.window, self))
        self.add_frame("login", LoginFrame(self.window, self))

        self.window.show_form()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        return frame
