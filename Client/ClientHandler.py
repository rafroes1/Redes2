class ClientHandler:

    def __init__(self, id, nick, ip, porta, conn):
        self.id = str(id)
        self.nick = str(nick)
        self.ip = str(ip)
        self.porta = str(porta)
        self.conn = conn

    def getConn(self):
        return self.conn

    def getId(self):
        return self.id

    def getNick(self):
        return self.nick