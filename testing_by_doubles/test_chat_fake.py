import unittest
from unittest import mock
from chat_client import ChatClient
from connection import Connection
from fakeserver import FakeServer

"""
Stubs, spies, and dummies are all about state.
Mocks are usually meant to keep track of behaviors. They usually crash when the software hasn't done what you expected. So they are usually meant to 
assert that they were used in a specific expected way, which confirms that the software behaved as we wished.
"""


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        user1 = ChatClient("John Doe")
        user2 = ChatClient("Harry Potter")

        user1.send_message("Hello World")
        messages = user2.fetch_messages()

        assert messages == ["John Doe: Hello World"]


class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")

        assert client.nickname == "User 1"

    def test_send_message(self):
        client = ChatClient("User 1")
        client.connection = unittest.mock.Mock()

        sent_message = client.send_message("Hello World")

        assert sent_message == "User 1: Hello World"

    def test_client_connection(self):
        client = ChatClient("User 1")

        connection_spy = unittest.mock.MagicMock()
        with unittest.mock.patch.object(
            client, "_get_connection", return_value=connection_spy
        ):
            client.send_message("Hello World")

        connection_spy.broadcast.assert_called_with(("User 1: Hello World"))


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")
            messages = c.get_messages()

        assert messages[-1] == "some message"

    def test_exchange_with_server(self):
        with unittest.mock.patch(
            "multiprocessing.managers.listener_client",
            new={"pickle": (None, FakeServer())},
        ):
            c1 = Connection(("localhost", 9090))
            c2 = Connection(("localhost", 9090))

            c1.broadcast("connected message")

            assert c2.get_messages()[-1] == "connected message"


if __name__ == "__main__":
    unittest.main()
