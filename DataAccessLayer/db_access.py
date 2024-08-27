import sqlite3
from CommonLayer.user import User
from CommonLayer.task import Task
from CommonLayer import global_variables


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
            if global_variables.current_user.role_id == 2:
                data = cursor.execute("""
                    SELECT Task.id,
                           Task.name,
                           Task.progress_status,
                           User.first_name || ' ' || User.last_name AS assigned_to,
                           Task.creation_date,
                           Task.start_date,
                           Task.due_date,
                           Task.completion_date,
                           Task.assigned_by,
                           Task.description
                    FROM Task
                    JOIN User ON Task.assigned_to = User.id
                    WHERE Task.assigned_by == ?""", (current_user_id,)).fetchall()
            else:
                data = cursor.execute("""
                                SELECT Task.id,
                                       Task.name,
                                       Task.progress_status,
                                       Task.assigned_to,
                                       Task.creation_date,
                                       Task.start_date,
                                       Task.due_date,
                                       Task.completion_date,
                                       User.first_name || ' ' || User.last_name AS assigned_to,
                                       Task.description
                                FROM Task
                                JOIN User ON Task.assigned_by = User.id
                                Where assigned_to ==  ?""", (current_user_id,)).fetchall()
            for item in data:
                task = Task.create_instance_tuple(item)
                task_list.append(task)

        return task_list

    def delete_task(self, task_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Task WHERE id = ?", (task_id,))
            connection.commit()

    def fetch_username(self):
        user_list = []
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
            Where role_id = ?
            """, (1,)).fetchall()

            for item in data:
                user = User.create_instance_tuple(item)
                user_list.append(user)

        return user_list

    def create_new_task(self, task):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO Task (name,
                              progress_status,
                              assigned_to,
                              creation_date,
                              start_date,
                              due_date,
                              completion_date,
                              assigned_by,
                              description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (task.name, task.progress_status, task.assigned_to, task.creation_date, task.start_date,
              task.due_date, task.completion_date, task.assigned_by, task.description))

            connection.commit()
