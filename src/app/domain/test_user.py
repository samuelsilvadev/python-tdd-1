from uuid import uuid4
from domain.user import User
import pytest


class TestUser:
    def test_create_an_user(serf):
        user_id = uuid4()
        user_name = 'Random Name'

        new_user = User(id=user_id, name=user_name)

        assert new_user.id == user_id
        assert new_user.name == user_name

    def test_validate_user_id(self):
        user_id = "invalid because it is a string"
        user_name = 'Random Name'

        with pytest.raises(Exception, match="Id must be a instance of UUID."):
            User(id=user_id, name=user_name)

    def test_validate_empty_user_name(self):
        user_id = uuid4()
        user_name = ""

        with pytest.raises(Exception, match="Name is required."):
            User(id=user_id, name=user_name)

    def test_validate_invalid_user_name(self):
        user_id = uuid4()
        user_name = 1

        with pytest.raises(Exception, match="Name must be a string."):
            User(id=user_id, name=user_name)
