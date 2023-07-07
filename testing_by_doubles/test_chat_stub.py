import unittest
from unittest import mock
from chat_client import ChatClient
from connection import Connection


class TestChatClient(unittest.TestCase):

    def test_send_message_using_stub(self):
        """
        Stubs provide canned answers, replacing those pieces of the software 
        with the ready-made state or answer that we could have got if it had 
        run for real. So we are going to replace Connection.get_messages 
        with a stub that returns an empty list and see that everything works
        """
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost",9090))
        with unittest.mock.patch.object(c,"get_messages",return_value =[]):
            c.broadcast("hello world")
            self.assertEqual(c.get_messages()[-1],"hello world")


if __name__ == "__main__":
    unittest.main()