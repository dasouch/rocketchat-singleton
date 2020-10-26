import os

import pytest

from rocketchat_API.rocketchat import RocketChat


@pytest.fixture(scope="function")
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
    rocket_chat = RocketChat(user_id=user.name, password=user.password)
    login = rocket_chat.login(user.name, user.password).json()
    response = rocket_chat.users_create_token(user_id=login.get("data").get("userId"))
    os.environ['ROCKET_CHAT_AUTH_TOKEN'] = response.json()['data']['authToken']
    os.environ['ROCKET_CHAT_USER_ID'] = response.json()['data']['userId']
