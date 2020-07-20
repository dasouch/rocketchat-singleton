import pytest

from rocketchat_API.rocketchat import RocketChat


@pytest.fixture(scope="session", autouse=True)
def create_user():
    user = type('test', (object,), {})()
    user.name = "rocket"
    user.password = "password"
    user.email = "dasouch@gmail.com"

    RocketChat().users_register(
        email=user.email,
        name=user.name,
        password=user.password,
        username=user.name
    )

