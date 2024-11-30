from uuid import UUID


class User:
    id: UUID
    name: str

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.validate_input()

    def validate_input(self):
        if not isinstance(self.id, UUID):
            raise Exception("Id must be a instance of UUID.")

        if not isinstance(self.name, str):
            raise Exception("Name must be a string.")

        if len(self.name) == 0:
            raise Exception("Name is required.")
