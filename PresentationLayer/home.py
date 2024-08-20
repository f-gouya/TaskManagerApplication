from ttkbootstrap import Frame, Label, Button
# from CommonLayer import global_variables


class HomeFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self)
        self.header.grid(row=0, column=0, pady=10)

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.profile_button = Button(self, text="My Profile", command=self.load_user_profile)
        self.profile_button.grid(row=2, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.user_management_button = Button(self, text="User Management", command=self.load_user_management)

        self.user_request_button = Button(self, text="User Request", command=self.load_user_request)

    def logout(self):
        # global_variables.current_user = None
        self.main_view.switch_frame("login")

    def set_home_user(self):
        pass
        # self.header.config(text=f"Welcome {global_variables.current_user}")
        # if global_variables.current_user.role_id == 2:
        #     self.user_management_button.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")
        #     self.user_request_button.grid(row=4, column=0, pady=(0, 10), padx=20, sticky="ew")
        # else:
        #     self.user_management_button.grid_remove()
        #     self.user_request_button.grid_remove()

    def load_user_management(self):
        frame = self.main_view.switch_frame("user_management")
        frame.set_management_user_info()

    def load_user_profile(self):
        frame = self.main_view.switch_frame("profile")
        # frame.show_user_information(global_variables.current_user)

    def load_user_request(self):
        frame = self.main_view.switch_frame("user_request")
        frame.set_user_request_info()
