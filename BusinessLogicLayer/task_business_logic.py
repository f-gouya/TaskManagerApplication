from CommonLayer.reponse import Response
from DataAccessLayer.db_access import DBAccess
from CommonLayer import global_variables
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
        if global_variables.current_user.role_id == 2:
            task_list = self.data_access.get_all_tasks(global_variables.current_user.id)
            return task_list
