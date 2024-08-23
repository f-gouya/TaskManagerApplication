from PresentationLayer.manage_form import ManageFrame


class ManagerManageForm(ManageFrame):
    def __init__(self, window, view):
        super().__init__(window, view)

        self.create_button.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.edit_button.grid(row=0, column=1, pady=10, padx=10)

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
