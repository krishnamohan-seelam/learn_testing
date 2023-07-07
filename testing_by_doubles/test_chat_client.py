import unittest
from unittest import mock
from chat_client import ChatClient

"""
A dummy is an object that does nothing. 
It just serves the purpose of being passed around as an argument and not making the code crash because we lack an object. 
But its implementation is totally empty; it does nothing.

To implement dummy objects we can use the Python unittest.mock module. 
"""


class DummyConnection(object):
    def broadcast(self, *args, **kwargs):
        return


class TestChatClient(unittest.TestCase):
    def test_name(self):
        mock_connection = unittest.mock.Mock()
        client = ChatClient("dummy_user", connection=mock_connection)
        self.assertEqual(client.nickname, "dummy_user")

    def test_send_message_using_dummy(self):
        """
        Test send message by creating dummy connection
        """
        connection = DummyConnection()
        client = ChatClient("user 1", connection)
        test_result = client.send_message("hello world")
        self.assertEqual(test_result, "user 1: hello world")

    def test_send_message_using_mock(self):
        """
        Test send message by creating dummy connection using mock
        """
        mock_connection = mock.Mock()
        client = ChatClient("user 1", mock_connection)
        test_result = client.send_message("hello world")
        self.assertEqual(test_result, "user 1: hello world")


if __name__ == "__main__":
    unittest.main()
