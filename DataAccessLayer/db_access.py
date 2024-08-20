import sqlite3
from CommonLayer.user import User
from CommonLayer.task import Task


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

    def get_all_tasks(self, current_user_id):
        task_list = []
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT id,
                   name,
                   progress_status,
                   assigned_to,
                   creation_date,
                   start_date,
                   due_date,
                   completion_date,
                   assigned_by,
                   description
            FROM Task
            Where assigned_by ==  ?""", (current_user_id,)).fetchall()
            for item in data:
                print(item)
                task = Task.create_instance_tuple(item)
                task_list.append(task)

        return task_list
