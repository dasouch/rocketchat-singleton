from rocketchat.main import RocketChatBot


def test_chat_post_message(create_user):
    with RocketChatBot() as rocket:
        response = rocket.chat_post_message('hello world', channel='GENERAL')
        assert response.json()['success'] is True
