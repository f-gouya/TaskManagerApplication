import sqlite3
from CommonLayer.user import User


class DBAccess:
    def __init__(self):
        self.database_name = "Data\\DB\\TMADB.db"

    def get_user(self, username, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   role_id
            FROM User
            Where username = ?
            And password = ?
            """, (username, password)).fetchone()

            if data:
                user = User.create_instance_tuple(data)
                return user
