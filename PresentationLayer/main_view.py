from PresentationLayer.window import Windows
from PresentationLayer.login import LoginFrame
from PresentationLayer.home import HomeFrame
from PresentationLayer.manager_manage_form import ManagerManageForm
from PresentationLayer.assignee_manage_form import AssigneeManageForm
from PresentationLayer.create_task_form import CreateTaskFrame
from PresentationLayer.edit_task_form import EditTaskFrame


class MainView:
    def __init__(self):
        self.window = Windows()

        self.frames = {}

        self.add_frame("edit_task_frame", EditTaskFrame(self.window, self))
        self.add_frame("create_task_frame", CreateTaskFrame(self.window, self))
        self.add_frame("manager_manage_frame", ManagerManageForm(self.window, self))
        self.add_frame("assignee_manage_frame", AssigneeManageForm(self.window, self))
        self.add_frame("home", HomeFrame(self.window, self))
        self.add_frame("login", LoginFrame(self.window, self))
        # self.add_frame("task_info_form", TaskInfoFrame(self.window, self))

        self.window.show_form()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        return frame
