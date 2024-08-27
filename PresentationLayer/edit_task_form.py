from PresentationLayer.task_info_form import TaskInfoFrame
from ttkbootstrap.dialogs import Messagebox
from CommonLayer import global_variables


class EditTaskFrame(TaskInfoFrame):
    def __init__(self, window, view):
        super().__init__(window, view)

        self.confirm_button.configure(command=self.edit_task)

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
