from multiprocessing.managers import SyncManager, ListProxy


class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages", proxytype=ListProxy)
        super().__init__(address=address, authkey=b"mychatsecret")
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)
