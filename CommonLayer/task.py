class Task:
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
