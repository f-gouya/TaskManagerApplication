from datetime import datetime


class DateValue:
    def __init__(self, allow_null=False, date_format="%Y-%m-%d"):
        self.allow_null = allow_null
        self.date_format = date_format

    def __set_name__(self, owner, name):
        self._attribute_name = name

    def __get__(self, instance, owner):
        value = instance.__dict__.get(self._attribute_name)
        if value is not None and isinstance(value, datetime):
            return value.strftime(self.date_format)
        return value

    def __set__(self, instance, value):
        if value == "" and not self.allow_null:
            raise ValueError(f"{self._attribute_name} cannot be None")
        if value != "":
            if isinstance(value, str):
                try:
                    value = datetime.strptime(value, self.date_format)
                except ValueError:
                    raise ValueError(f"{self._attribute_name} must be in the format {self.date_format}")
            elif not isinstance(value, datetime):
                raise ValueError(f"{self._attribute_name}"
                                 f" must be a datetime object or a string in the format {self.date_format}")
        instance.__dict__[self._attribute_name] = value


class StrValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self._attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attribute_name]

    def __set__(self, instance, value):
        if (not isinstance(value, str) or len(value) < self.min_length
                or len(value) > self.max_length):
            raise ValueError("The task name must be at least 3 characters.\nThe description can't be empty.")
        else:
            instance.__dict__[self._attribute_name] = value


class Task:
    name = StrValue(3, 50)
    description = StrValue(3, 200)
    creation_date = DateValue()
    start_date = DateValue()
    due_date = DateValue()
    completion_date = DateValue(allow_null=True)

    def __init__(self, tid, name, progress_status, assigned_to, creation_date,
                 start_date, due_date, completion_date, assigned_by, description):
        self.id = tid
        self.name = name
        self.progress_status = progress_status
        self.assigned_to = assigned_to
        self.creation_date = creation_date
        self.start_date = start_date
        self.due_date = due_date
        self.completion_date = completion_date
        self.assigned_by = assigned_by
        self.description = description

    @classmethod
    def create_instance_tuple(cls, data_tuple):
        return cls(data_tuple[0], data_tuple[1], data_tuple[2], data_tuple[3], data_tuple[4],
                   data_tuple[5], data_tuple[6], data_tuple[7], data_tuple[8], data_tuple[9])
