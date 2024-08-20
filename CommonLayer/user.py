class User:
    def __init__(self, uid, firstname, lastname, username, password, role_id):
        self.id = uid
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.role_id = role_id

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @classmethod
    def create_instance_tuple(cls, data_tuple):
        return cls(data_tuple[0], data_tuple[1], data_tuple[2], data_tuple[3], data_tuple[4], data_tuple[5])
