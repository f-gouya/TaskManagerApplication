from ttkbootstrap import Frame, LabelFrame, Label, Button, Entry, Radiobutton, Treeview, Scrollbar, VERTICAL, StringVar
from BusinessLogicLayer.task_business_logic import TaskBusinessLogic
from CommonLayer import global_variables
from datetime import datetime


class ManageFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.row_list = []
        self.task_business = TaskBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.manage_form_frame = LabelFrame(self, text="Manage Tasks", padding=10)
        self.manage_form_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.manage_form_frame.grid_columnconfigure([index for index in range(4)], weight=1)

        self.create_button = Button(self.manage_form_frame, text="Create", width=15)

        self.edit_button = Button(self.manage_form_frame, text="Edit", width=15, command=self.load_edit_task_frame)

        self.delete_button = Button(self.manage_form_frame, text="Delete", width=15)

        self.back_button = Button(self.manage_form_frame, text="Back", width=15, command=self.show_home_frame)

        self.search_entry = Entry(self.manage_form_frame, width=30)
        self.search_entry.grid(row=1, column=0, columnspan=4, pady=(0, 10), padx=10, sticky="ew")
        self.search_entry.bind("<KeyRelease>", self.search)

        self.filter_var = StringVar(value="all")

        self.radio_frame = Label(self.manage_form_frame)
        self.radio_frame.grid(row=2, column=0,columnspan=4, pady=10, padx=10, sticky="nsew")
        self.radio_frame.grid_columnconfigure(0, weight=1)
        self.radio_frame.grid_columnconfigure(1, weight=1)
        self.radio_frame.grid_columnconfigure(2, weight=1)
        self.radio_frame.grid_columnconfigure(3, weight=1)

        self.radio_all = Radiobutton(self.radio_frame, text="Show all Tasks", variable=self.filter_var,
                                     value="all", command=self.filter_tasks)
        self.radio_today = Radiobutton(self.radio_frame, text="Show today's Tasks", variable=self.filter_var,
                                       value="today", command=self.filter_tasks)
        self.radio_in_progress = Radiobutton(self.radio_frame, text="Show in-progress Tasks",
                                             variable=self.filter_var, value="in_progress", command=self.filter_tasks)
        self.radio_done = Radiobutton(self.radio_frame, text="Show done Tasks", variable=self.filter_var,
                                      value="done", command=self.filter_tasks)

        self.radio_all.grid(row=0, column=0, padx=5)
        self.radio_today.grid(row=0, column=1, padx=5)
        self.radio_in_progress.grid(row=0, column=2, padx=5)
        self.radio_done.grid(row=0, column=3, padx=5)

        self.task_table = Treeview(self)

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.task_table.yview)
        self.scrollbar.grid(row=3, column=1, sticky='ns')

    def search(self, _):
        self.filter_var.set("all")
        term = self.search_entry.get().lower()
        task_list = self.task_business.search(term)
        self.fill_table(task_list)

    def load_edit_task_frame(self):
        task_id_list = self.task_table.selection()
        task_list = self.load_data()
        if task_id_list:
            selected_task_id = task_id_list[0]
            frame = self.main_view.switch_frame("edit_task_frame")
            task_info = next(task for task in task_list if int(task.id) == int(selected_task_id))
            frame.fill_task_widget(task_info)

    def set_task_info(self):
        self.filter_var.set("all")
        task_list = self.load_data()
        self.fill_table(task_list)

    def load_data(self):
        task_list = self.task_business.get_tasks()
        return task_list

    def fill_table(self, task_list):
        for row in self.row_list:
            self.task_table.delete(row)
        self.row_list.clear()

        row_number = 1
        for task in task_list:
            row = self.task_table.insert("",
                                         "end",
                                         iid=task.id,
                                         text=str(row_number),
                                         values=(row_number, task.name.capitalize(),
                                                 task.progress_status,
                                                 ' '.join([word.capitalize() for word in task.assigned_to.split()])
                                                 if
                                                 global_variables.current_user.role_id == 2
                                                 else
                                                 ' '.join([word.capitalize() for word in task.assigned_by.split()]),
                                                 task.creation_date,
                                                 task.start_date, task.due_date, task.completion_date))
            self.row_list.append(row)
            row_number += 1

    def filter_tasks(self):
        filter_option = self.filter_var.get()
        task_list = self.load_data()

        if filter_option == "today":
            task_list = [task for task in task_list if
                         task.creation_date == datetime.now().strftime('%Y-%m-%d')]
        elif filter_option == "in_progress":
            task_list = [task for task in task_list if task.progress_status < 100]
        elif filter_option == "done":
            task_list = [task for task in task_list if task.progress_status == 100]

        self.fill_table(task_list)

    def show_home_frame(self):
        self.search_entry.delete(0, "end")
        frame = self.main_view.switch_frame("home")
        frame.set_home_user()
