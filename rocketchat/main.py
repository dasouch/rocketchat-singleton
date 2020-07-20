from rocketchat_API.rocketchat import RocketChat

from rocketchat.settings import ROCKET_CHAT_URL, ROCKET_CHAT_PASSWORD, ROCKET_CHAT_USERNAME


class RocketChatBot:
    _instance = None
    rocket = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.rocket = RocketChat(ROCKET_CHAT_USERNAME, ROCKET_CHAT_PASSWORD, server_url=ROCKET_CHAT_URL)
            cls._instance = object.__new__(cls)
        return cls._instance

    def __enter__(self):
        return self.rocket

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
