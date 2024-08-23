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
            else:
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
                                Where assigned_to ==  ?""", (current_user_id,)).fetchall()
            for item in data:
                task = Task.create_instance_tuple(item)
                task_list.append(task)

        return task_list

    # def search(self, term):
    #     task_list = []
    #     with sqlite3.connect(self.database_name) as connection:
    #         cursor = connection.cursor()
    #         if global_variables.current_user.role_id == 2:
    #             query = """
    #             SELECT id,
    #                    name,
    #                    progress_status,
    #                    assigned_to,
    #                    creation_date,
    #                    start_date,
    #                    due_date,
    #                    completion_date,
    #                    assigned_by,
    #                    description
    #             FROM Task
    #             WHERE assigned_by == ?
    #             AND name LIKE ?
    #             OR assigned_to LIKE ?
    #             """
    #             cursor.execute(query, (global_variables.current_user.id, f"%{term}%", f"%{term}%"))
    #         else:
    #             query = """
    #                             SELECT id,
    #                                    name,
    #                                    progress_status,
    #                                    assigned_to,
    #                                    creation_date,
    #                                    start_date,
    #                                    due_date,
    #                                    completion_date,
    #                                    assigned_by,
    #                                    description
    #                             FROM Task
    #                             WHERE assigned_to == ?
    #                             AND name LIKE ?
    #                             OR assigned_by LIKE ?
    #                             """
    #             cursor.execute(query, (global_variables.current_user.id, f"%{term}%", f"%{term}%"))
    #         data = cursor.fetchall()
    #
    #         for item in data:
    #             task = Task.create_instance_tuple(item)
    #             task_list.append(task)
    #
    #     return task_list
