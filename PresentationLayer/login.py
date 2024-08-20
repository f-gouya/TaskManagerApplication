from ttkbootstrap import Frame, Label, Entry, Button, LabelFrame, PhotoImage
from ttkbootstrap.dialogs import Messagebox


class LoginFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.logo = PhotoImage(file="Data\\Images\\task_manager_logo.png")
        self.logo_label = Label(self, image=self.logo)
        self.logo_label.grid(row=1, column=0, pady=10)

        self.login_form_frame = LabelFrame(self, text="Sign in", padding=10)
        self.login_form_frame.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

        self.login_form_frame.grid_columnconfigure(0, weight=1)

        self.username_label = Label(self.login_form_frame, text="Username")
        self.username_label.grid(row=0, column=0, padx=10, sticky="w")

        self.username_entry = Entry(self.login_form_frame)
        self.username_entry.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")
        self.username_entry.bind("<Return>", lambda _: self.login())

        self.password_label = Label(self.login_form_frame, text="Password")
        self.password_label.grid(row=2, column=0, padx=10, sticky="w")

        self.password_entry = Entry(self.login_form_frame, show="*")
        self.password_entry.grid(row=3, column=0, pady=(0, 15), padx=10, sticky="ew")
        self.password_entry.bind("<Return>", lambda _: self.login())

        self.login_button = Button(self, text="Login", width=15, command=self.login)
        self.login_button.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

    def login(self):
        username = self.username_entry.get().lower()
        password = self.password_entry.get()

        # user_business = UserBusinessLogic()
        # response = user_business.login(username, password)

        # if not response.success:
        #     Messagebox.show_error(response.message, "Error")
        # else:
        #     self.clear_login_entry()
        #     home_frame = self.main_view.switch_frame("home")
        #     global_variables.current_user = response.data
        #     home_frame.set_home_user()

    def clear_login_entry(self):
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
