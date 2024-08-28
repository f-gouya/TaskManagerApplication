from PresentationLayer.task_info_form import TaskInfoFrame
from ttkbootstrap.dialogs import Messagebox
from CommonLayer import global_variables


class EditTaskFrame(TaskInfoFrame):
    def __init__(self, window, view):
        super().__init__(window, view)

        self.task_label.config(text="Edit Tasks")
        self.task_progress_label.grid(row=2, column=2, pady=10, padx=10, sticky="w")
        self.task_progress_entry.grid(row=2, column=3, pady=10, padx=10, sticky="ew")
        self.confirm_button.configure(command=self.edit_task)

    def fill_task_widget(self, task_info):
        self.task_name_entry.config(state='normal')
        self.task_name_entry.insert("end", task_info.name)
        self.task_name_entry.config(state='readonly')
        self.task_progress_entry.config(state='normal')
        self.task_progress_entry.delete(0, "end")
        self.task_progress_entry.insert("end", task_info.progress_status)
        if task_info.progress_status == 100:
            self.task_progress_entry.config(state='readonly')
        self.assignee_combobox.config(state='normal')
        if global_variables.current_user.role_id == 2:
            self.assignee_label.config(text="Assigned to")
            self.assignee_combobox.set(' '.join([word.capitalize() for word in task_info.assigned_to.split()]))
        else:
            self.assignee_label.config(text="Assigned by")
            self.assignee_combobox.set(' '.join([word.capitalize() for word in task_info.assigned_by.split()]))
        self.assignee_combobox.config(state='readonly')
        self.from_date_entry.entry.config(state='normal')
        self.from_date_entry.entry.delete(0, "end")
        self.from_date_entry.entry.insert(0, task_info.start_date)
        self.from_date_entry.entry.config(state='readonly')
        self.to_date_entry.entry.config(state='normal')
        self.to_date_entry.entry.delete(0, "end")
        self.to_date_entry.entry.insert(0, task_info.due_date)
        self.to_date_entry.entry.config(state='readonly')
        self.task_description_text.config(state='normal')
        self.task_description_text.insert('1.0', task_info.description)
        self.task_description_text.config(state='disabled')

    def edit_task(self):
        task_name = self.task_name_entry.get()
        assigned_to = self.assignee_combobox.get()
        if assigned_to:
            assigned_to = next(user.id for user in self.user_list if self.assignee_combobox.get() == str(user))
        start_date = self.from_date_entry.entry.get()
        due_date = self.to_date_entry.entry.get()
        assigned_by = global_variables.current_user.id
        description = self.task_description_text.get("1.0", "end").strip()

        response = self.task_business.create_task(task_name, assigned_to, start_date,
                                                  due_date, assigned_by, description)

        if not response.success:
            Messagebox.show_error(response.message, "Warning")
        else:
            Messagebox.show_info(response.message, "Info")
            self.clear_widget()
