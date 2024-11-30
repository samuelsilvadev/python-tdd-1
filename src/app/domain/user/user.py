from uuid import UUID
from typing import List
from domain.task.task import Task


class User:
    id: UUID
    name: str
    tasks: List[Task]

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.tasks = []
        self.validate_input()

    def validate_input(self):
        if not isinstance(self.id, UUID):
            raise Exception("Id must be a instance of UUID.")

        if not isinstance(self.name, str):
            raise Exception("Name must be a string.")

        if len(self.name) == 0:
            raise Exception("Name is required.")

    def add_tasks(self, tasks: List[Task]):
        self.tasks.extend(tasks)
