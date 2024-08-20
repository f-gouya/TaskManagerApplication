from CommonLayer.reponse import Response
from DataAccessLayer.db_access import DBAccess
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
