class NameValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self._attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attribute_name]

    def __set__(self, instance, value):
        if (not isinstance(value, str) or len(value) < self.min_length
                or len(value) > self.max_length or not value.isalpha()):
            raise ValueError("The first name and lastname must be at least 3 characters and contain only letters.")
        else:
            instance.__dict__[self._attribute_name] = value


class User:
    first_name = NameValue(3, 20)
    last_name = NameValue(3, 20)

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
