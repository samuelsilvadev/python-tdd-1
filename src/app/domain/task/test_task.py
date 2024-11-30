from uuid import uuid4
from domain.task.task import Task
import pytest


class TestTask:
    def test_create_task(self):
        task_id = uuid4()
        user_id = uuid4()
        name = "task name"
        description = "task description"
        completed = True

        new_task = Task(id=task_id, user_id=user_id, name=name,
                        description=description, completed=completed)

        assert new_task.id == task_id
        assert new_task.user_id == user_id
        assert new_task.name == name
        assert new_task.description == description
        assert new_task.completed == completed

    def test_create_task_without_all_arguments(self):
        task_id = uuid4()
        user_id = uuid4()
        name = "task name"

        new_task = Task(id=task_id, user_id=user_id, name=name)

        assert new_task.id == task_id
        assert new_task.user_id == user_id
        assert new_task.name == name
        assert new_task.description == ""
        assert new_task.completed == False

    def test_validate_task_id(self):
        task_id = "Invalid task id"
        user_id = uuid4()
        name = "task name"
        description = "task description"
        completed = True

        with pytest.raises(Exception, match="Task Id must be a instance of UUID."):
            Task(id=task_id, user_id=user_id, name=name,
                 description=description, completed=completed)

    def test_validate_user_id(self):
        task_id = uuid4()
        user_id = "Invalid user id"
        name = "task name"
        description = "task description"
        completed = True

        with pytest.raises(Exception, match="User Id must be a instance of UUID."):
            Task(id=task_id, user_id=user_id, name=name,
                 description=description, completed=completed)

    def test_validate_user_id_as_integer(self):
        task_id = uuid4()
        user_id = 1
        name = "task name"
        description = "task description"
        completed = True

        with pytest.raises(Exception, match="User Id must be a instance of UUID."):
            Task(id=task_id, user_id=user_id, name=name,
                 description=description, completed=completed)

    def test_validate_task_name(self):
        task_id = uuid4()
        user_id = uuid4()
        name = ""
        description = "task description"
        completed = True

        with pytest.raises(Exception, match="Task name is required."):
            Task(id=task_id, user_id=user_id, name=name,
                 description=description, completed=completed)

    def test_validate_task_completed_status(self):
        task_id = uuid4()
        user_id = uuid4()
        name = "task name"
        description = "task description"
        completed = 1

        with pytest.raises(Exception, match="Task completed status must be a boolean."):
            Task(id=task_id, user_id=user_id, name=name,
                 description=description, completed=completed)

    def test_that_task_is_marked_as_completed(self):
        task_id = uuid4()
        user_id = uuid4()
        name = "task name"
        description = "task description"
        completed = False

        task = Task(id=task_id, user_id=user_id, name=name,
                    description=description, completed=completed)

        assert task.completed == False

        task.mark_as_completed()

        assert task.completed == True

    def test_that_task_is_marked_as_incomplete(self):
        task_id = uuid4()
        user_id = uuid4()
        name = "task name"
        description = "task description"
        completed = False

        task = Task(id=task_id, user_id=user_id, name=name,
                    description=description, completed=completed)

        assert task.completed == False

        task.mark_as_completed()
        task.mark_as_incomplete()

        assert task.completed == False
