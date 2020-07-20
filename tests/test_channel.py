from rocketchat.main import RocketChatBot


def test_channels_list():
    with RocketChatBot() as rocket:
        response = rocket.chat_post_message('hello world', channel='GENERAL')
        assert response.json()['success'] is True
