from ttkbootstrap import Frame, Label, LabelFrame, Button, Entry, DateEntry, Combobox, Text
from BusinessLogicLayer.task_business_logic import TaskBusinessLogic
from CommonLayer import global_variables
from datetime import datetime


class TaskInfoFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.task_business = TaskBusinessLogic()
        self.user_list = []
        self.widget_list = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.task_label = LabelFrame(self, padding=15)
        self.task_label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.task_label.grid_columnconfigure(1, weight=1)
        self.task_label.grid_columnconfigure(3, weight=1)
        self.task_label.grid_rowconfigure(3, weight=1)

        self.task_name_label = Label(self.task_label, text="Task Name")
        self.task_name_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.task_name_entry = Entry(self.task_label)
        self.task_name_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")
        self.widget_list.append(self.task_name_entry)

        self.assignee_label = Label(self.task_label)
        self.assignee_label.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        self.assignee_combobox = Combobox(self.task_label, state='readonly')
        self.assignee_combobox.grid(row=0, column=3, pady=10, padx=10, sticky="ew")
        self.widget_list.append(self.assignee_combobox)

        self.from_date_label = Label(self.task_label, text="From")
        self.from_date_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.from_date_entry = DateEntry(self.task_label, dateformat='%Y-%m-%d')
        self.from_date_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")
        self.widget_list.append(self.from_date_entry.entry)

        self.to_date_label = Label(self.task_label, text="To")
        self.to_date_label.grid(row=1, column=2, pady=10, padx=10, sticky="w")

        self.to_date_entry = DateEntry(self.task_label, dateformat='%Y-%m-%d')
        self.to_date_entry.grid(row=1, column=3, pady=10, padx=10, sticky="ew")
        self.widget_list.append(self.to_date_entry.entry)

        self.task_description_label = Label(self.task_label, text="Description")
        self.task_description_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        self.task_progress_label = Label(self.task_label, text="Progress status")

        self.task_progress_entry = Entry(self.task_label)
        self.widget_list.append(self.task_progress_entry)

        self.task_description_text = Text(self.task_label, height=5)
        self.task_description_text.grid(row=3, column=0, columnspan=4, pady=(0, 10), padx=10, sticky="ew")
        self.widget_list.append(self.task_description_text)

        self.confirm_button = Button(self.task_label, text="Confirm", width=15)
        self.confirm_button.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        self.back_button = Button(self.task_label, text="Back", width=15, command=self.show_manage_frame)
        self.back_button.grid(row=4, column=3, pady=10, padx=10, sticky="e")

    def fetch_username(self):
        self.confirm_button.configure(state="normal")
        self.user_list = self.task_business.fetch_assignee_username()
        self.user_list = sorted(self.user_list, key=str)
        self.assignee_combobox.configure(values=self.user_list)

    def show_manage_frame(self):
        self.confirm_button.configure(state="disabled")
        if global_variables.current_user.role_id == 2:
            frame = self.main_view.switch_frame("manager_manage_frame")
        else:
            frame = self.main_view.switch_frame("assignee_manage_frame")
        frame.set_task_info()
        self.clear_widget()

    def clear_widget(self):
        self.task_name_entry.delete(0, "end")
        self.assignee_combobox.set('')
        self.task_progress_entry.delete(0, "end")

        current_date = datetime.now().strftime('%Y-%m-%d')

        self.from_date_entry.entry.delete(0, "end")
        self.from_date_entry.entry.insert(0, current_date)
        self.to_date_entry.entry.delete(0, "end")
        self.to_date_entry.entry.insert(0, current_date)
        self.task_description_text.delete('1.0', "end")
