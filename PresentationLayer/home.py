from ttkbootstrap import Frame, Label, Button
from CommonLayer import global_variables


class HomeFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self)
        self.header.grid(row=0, column=0, pady=10)

        self.manage_button = Button(self, text="Manage")
        self.manage_button.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")

        # self.report_button = Button(self, text="Report", command=self.logout)
        # self.report_button.grid(row=2, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")

    def logout(self):
        global_variables.current_user = None
        self.main_view.switch_frame("login")

    def set_home_user(self):
        self.header.config(text=f"Welcome {global_variables.current_user}")
        if global_variables.current_user.role_id == 2:
            self.manage_button.config(command=self.load_manager_manage_frame)
        else:
            self.manage_button.config(command=self.load_assignee_manage_frame)

    def load_manager_manage_frame(self):
        frame = self.main_view.switch_frame("manager_manage_frame")
        frame.set_task_info()

    def load_assignee_manage_frame(self):
        frame = self.main_view.switch_frame("assignee_manage_frame")
        frame.set_task_info()
