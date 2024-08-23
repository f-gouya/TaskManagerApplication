from ttkbootstrap import Frame, LabelFrame, Button, Entry, Treeview, Scrollbar, VERTICAL
from BusinessLogicLayer.task_business_logic import TaskBusinessLogic
from CommonLayer import global_variables


class ManageFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.row_list = []
        self.task_business = TaskBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.manage_form_frame = LabelFrame(self, text="Manage Tasks", padding=15)
        self.manage_form_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.manage_form_frame.grid_columnconfigure([index for index in range(4)], weight=1)

        self.create_button = Button(self.manage_form_frame, text="Create", width=15, command=None)

        self.edit_button = Button(self.manage_form_frame, text="Edit", width=15, command=None)

        self.delete_button = Button(self.manage_form_frame, text="Delete", width=15, command=None)

        self.back_button = Button(self.manage_form_frame, text="Back", width=15, command=self.show_home_frame)

        self.search_entry = Entry(self.manage_form_frame, width=30)
        self.search_entry.grid(row=1, column=0, columnspan=4, pady=(0, 10), padx=10, sticky="ew")
        self.search_entry.bind("<KeyRelease>", self.search)

        self.task_table = Treeview(self)

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.task_table.yview)
        self.scrollbar.grid(row=3, column=1, sticky='ns')

    def search(self, _):
        term = self.search_entry.get().lower()
        task_list = self.task_business.search(term)
        self.fill_table(task_list)

    def set_task_info(self):
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
                                                 task.assigned_to if global_variables.current_user.role_id == 2
                                                 else task.assigned_by, task.creation_date,
                                                 task.start_date, task.due_date, task.completion_date))
            self.row_list.append(row)
            row_number += 1

    def show_home_frame(self):
        self.search_entry.delete(0, "end")
        frame = self.main_view.switch_frame("home")
        frame.set_home_user()
