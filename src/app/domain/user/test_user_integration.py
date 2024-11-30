from domain.user.user import User
from domain.task.task import Task
from uuid import uuid4


class TestUserIntegration:
    def test_user_add_tasks(self):

        user = User(id=uuid4(), name="Zeus")
        task_1 = Task(id=uuid4(), user_id=user.id,
                      name="learn how to program in go")
        task_2 = Task(id=uuid4(), user_id=user.id,
                      name="create my first website using claude")

        user.add_tasks([task_1, task_2])

        assert len(user.tasks) == 2
        assert task_1 in user.tasks
        assert task_2 in user.tasks

    def test_user_remove_task(self):

        user = User(id=uuid4(), name="Zeus")
        task_1 = Task(id=uuid4(), user_id=user.id,
                      name="learn how to program in go")

        user.add_tasks([task_1])
        user.remove_task(task_id=task_1.id)

        assert len(user.tasks) == 0
        assert task_1 not in user.tasks
