from PresentationLayer.manage_form import ManageFrame
from ttkbootstrap.dialogs import Messagebox


class ManagerManageForm(ManageFrame):
    def __init__(self, window, view):
        super().__init__(window, view)

        self.create_button.configure(command=self.load_create_task_frame)
        self.create_button.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.edit_button.grid(row=0, column=1, pady=10, padx=10)

        self.delete_button.configure(command=self.delete_task)
        self.delete_button.grid(row=0, column=2, pady=10, padx=10)

        self.back_button.grid(row=0, column=3, pady=10, padx=10, sticky="e")

        task_column = ("No", "Name", "Progress Status", "Assigned to", "Creation Date",
                       "Start Date", "Due Date", "Completion Date")

        self.task_table.configure(columns=task_column, show='headings')
        self.task_table.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="nsew")
        self.task_table.configure(yscrollcommand=self.scrollbar.set)

        for column in task_column:
            self.task_table.heading(column, text=column, anchor="center")
            self.task_table.column(column, anchor="center")

    def load_create_task_frame(self):
        frame = self.main_view.switch_frame("create_task_frame")
        frame.fetch_username()

    def delete_task(self):
        task_id_list = self.task_table.selection()
        response = self.task_business.delete_selected_task(task_id_list)
        Messagebox.show_info(response.message, "Info")

        task_list = self.load_data()
        self.fill_table(task_list)
