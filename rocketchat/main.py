import os

from rocketchat_API.rocketchat import RocketChat

from rocketchat.settings import ROCKET_CHAT_URL


class RocketChatBot:
    _instance = None
    rocket = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.rocket = RocketChat(user_id=os.environ['ROCKET_CHAT_USER_ID'],
                                    auth_token=os.environ['ROCKET_CHAT_AUTH_TOKEN'], server_url=ROCKET_CHAT_URL)
            cls._instance = object.__new__(cls)
        return cls._instance

    def __enter__(self):
        return self.rocket

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
