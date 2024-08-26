from CommonLayer.reponse import Response
from DataAccessLayer.db_access import DBAccess
from CommonLayer import global_variables
from CommonLayer.task import Task
from datetime import datetime
import hashlib


class TaskBusinessLogic:
    def __init__(self):
        self.data_access = DBAccess()

    def login(self, username, password):
        if not username or not password:
            return Response(None, False, "Invalid inputs.")
        hash_password = self.password_hashing(password)
        user = self.data_access.get_user(username, hash_password)
        if not user:
            return Response(None, False, "Invalid username or password.")
        return Response(user, True)

    @staticmethod
    def password_hashing(password):
        hash_string = hashlib.md5(password.encode())
        hash_password = hash_string.hexdigest()
        return hash_password

    def get_tasks(self):
        task_list = self.data_access.get_all_tasks(global_variables.current_user.id)
        return task_list

    def search(self, term):
        task_list = self.data_access.get_all_tasks(global_variables.current_user.id)
        search_list = []
        for task in task_list:
            if global_variables.current_user.role_id == 2:
                if term in task.name.lower() or term in task.assigned_to:
                    search_list.append(task)
            else:
                if term in task.name.lower() or term in task.assigned_by:
                    search_list.append(task)
        return search_list

    def delete_selected_task(self, task_id_list):
        if global_variables.current_user.role_id == 2:
            for task_id in task_id_list:
                self.data_access.delete_task(task_id)

    def fetch_assignee_username(self):
        username_list = []
        if global_variables.current_user.role_id == 2:
            username_list = self.data_access.fetch_username()
        return username_list

    def create_task(self, task_name, assigned_to, start_date, due_date, assigned_by, description):
        try:
            task_info = Task(None, task_name, 0, assigned_to, datetime.now().strftime("%Y-%m-%d"),
                             start_date, due_date, "", assigned_by, description)
        except ValueError as e:
            return Response(None, False, f"{e}")
        else:
            self.data_access.create_new_task(task_info)
            return Response(None, True, f"The Task is created successfully.")
