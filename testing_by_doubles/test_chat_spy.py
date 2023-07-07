import unittest
from unittest import mock
from chat_client import ChatClient
from connection import Connection

"""
spy, a kind of dummy object that, instead of doing nothing, actually records 
how it was called (if it was) and with which arguments.
"""


class TestChatClientSpyAcceptance(unittest.TestCase):
    def test_client_connection(self):
        client = ChatClient("User 1")

        connection_spy = unittest.mock.MagicMock()
        with unittest.mock.patch.object(
            client, "_get_connection", return_value=connection_spy
        ):
            client.send_message("Hello World")

        # assert that the spy was called with the
        # expected data to broadcast.
        connection_spy.broadcast.assert_called_with(("User 1: Hello World"))


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        user1 = ChatClient("John Doe")
        user2 = ChatClient("Harry Potter")

        user1.send_message("Hello World")
        messages = user2.fetch_messages()

        assert messages == ["John Doe: Hello World"]


if __name__ == "__main__":
    unittest.main()
