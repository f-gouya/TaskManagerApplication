from PresentationLayer.task_info_form import TaskInfoFrame
from ttkbootstrap.dialogs import Messagebox
from CommonLayer import global_variables


class EditTaskFrame(TaskInfoFrame):
    task_id = None

    def __init__(self, window, view):
        super().__init__(window, view)

        self.task_label.config(text="Edit Tasks")
        self.task_progress_label.grid(row=2, column=2, pady=10, padx=10, sticky="w")
        self.task_progress_entry.grid(row=2, column=3, pady=10, padx=10, sticky="ew")
        self.task_progress_entry.bind("<KeyRelease>", self.enable_confirm_button)
        self.confirm_button.configure(command=self.edit_task, state="disabled")

    def fill_task_widget(self, task_info):
        for widget in self.widget_list:
            widget.config(state="normal")

        self.clear_widget()

        EditTaskFrame.task_id = task_info.id

        if global_variables.current_user.role_id == 2:
            self.assignee_label.config(text="Assigned to")
            self.assignee_combobox.set(' '.join([word.capitalize() for word in task_info.assigned_to.split()]))
        else:
            self.assignee_label.config(text="Assigned by")
            self.assignee_combobox.set(' '.join([word.capitalize() for word in task_info.assigned_by.split()]))

        self.task_name_entry.insert("end", task_info.name)

        self.task_progress_entry.delete(0, "end")
        self.task_progress_entry.insert("end", task_info.progress_status)

        self.from_date_entry.entry.delete(0, "end")
        self.from_date_entry.entry.insert(0, task_info.start_date)

        self.to_date_entry.entry.delete(0, "end")
        self.to_date_entry.entry.insert(0, task_info.due_date)

        self.task_description_text.insert('1.0', task_info.description)

        for widget in self.widget_list:
            if widget != self.task_description_text:
                widget.config(state="readonly")
            else:
                widget.config(state="disabled")

        if task_info.progress_status != 100:
            self.task_progress_entry.config(state='normal')

    def edit_task(self):
        new_progress_status = int(self.task_progress_entry.get())
        response = self.task_business.edit_task(EditTaskFrame.task_id, new_progress_status)

        if not response.success:
            Messagebox.show_error(response.message, "Warning")
        else:
            Messagebox.show_info(response.message, "Info")
            self.show_manager_frame()
            self.confirm_button.configure(state="disabled")

    def enable_confirm_button(self, event):
        self.confirm_button.config(state="normal")
