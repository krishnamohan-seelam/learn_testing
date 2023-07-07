from connection import Connection


class ChatClient(object):
    def __init__(self, nickname, connection=None):
        self.nickname = nickname
        self._connection = connection
        self._last_msg_idx = 0

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(sent_message)
        return sent_message

    def fetch_messages(self):
        messages = list(self.connection.get_messages())
        new_messages = messages[self._last_msg_idx :]
        self._last_msg_idx = len(messages)
        return new_messages

    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._get_connection()
        return self._connection

    @connection.setter
    def connection(self, value):
        if self._connection is not None:
            self._connection.close()
        self._connection = value

    def _get_connection(self):
        return Connection(("localhost", 9090))
