from uuid import UUID


class Task:
    id: UUID
    user_id: UUID
    name: str
    description: str
    completed: bool

    def __init__(self, id, user_id, name, description, completed):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.completed = completed

        self.validate_input()

    def validate_input(self):
        if not isinstance(self.id, UUID):
            raise Exception("Task Id must be a instance of UUID.")

        if not isinstance(self.user_id, UUID):
            raise Exception("User Id must be a instance of UUID.")

        if len(self.name) == 0:
            raise Exception("Task name is required.")

        if not isinstance(self.completed, bool):
            raise Exception("Task completed status must be a boolean.")
