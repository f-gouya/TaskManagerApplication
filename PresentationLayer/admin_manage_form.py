from ttkbootstrap import Frame, Label, Button, Entry, Treeview, Scrollbar, VERTICAL
from BusinessLogicLayer.task_business_logic import TaskBusinessLogic


class AdminManageFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.row_list = []
        self.user_business = TaskBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text="User Management Form")
        self.header.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.back_button = Button(self, text="Back", width=15, command=self.show_home_frame)
        self.back_button.grid(row=0, column=0, pady=10, padx=10, sticky="e")

        self.search_entry = Entry(self, width=30)
        self.search_entry.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")
        self.search_entry.bind("<KeyRelease>", self.search)

        self.activate_button = Button(self, text="Activate", width=15, command=None)
        self.activate_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.deactivate_button = Button(self, text="Deactivate", width=15, command=None)
        self.deactivate_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        task_column = ("NO", "Name", "Progress Status", "Assigned to", "Creation Date",
                       "Start Date", "Due Date", "Completion Date")

        self.task_table = Treeview(self, columns=task_column)
        self.task_table.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="nsew")

        [self.task_table.heading(f"#{i}", text=task_column[i]) for i in range(len(task_column))]

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.task_table.yview)
        self.scrollbar.grid(row=3, column=1, sticky='ns')
        self.task_table.configure(yscrollcommand=self.scrollbar.set)

    def search(self, _):
        term = self.search_entry.get().lower()
        # user_list = self.user_business.search(term)
        # self.fill_table(user_list)
        #
        # user_list = self.load_data()
        # self.fill_table(user_list)

    def set_task_info(self):
        task_list = self.load_data()
        self.fill_table(task_list)

    def load_data(self):
        task_list = self.user_business.get_tasks()
        return task_list

    def fill_table(self, task_list):
        for row in self.row_list:
            self.task_table.delete(row)
        self.row_list.clear()

        row_number = 2
        for task in task_list:
            row = self.task_table.insert("",
                                         "end",
                                         iid=task.id,
                                         text=str(row_number),
                                         values=(task.name.capitalize(),
                                                 task.progress_status, task.assigned_to, task.creation_date,
                                                 task.start_date, task.due_date, task.completion_date))
            self.row_list.append(row)
            row_number += 1

    def show_home_frame(self):
        self.search_entry.delete(0, "end")
        frame = self.main_view.switch_frame("home")
        frame.set_home_user()
