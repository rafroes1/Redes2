import rsa

class ClientHandler:

    def __init__(self, id, nick, ip, porta, conn):
        self.id = str(id)
        self.nick = str(nick)
        self.ip = str(ip)
        self.porta = str(porta)
        self.conn = conn
        (self.pub_key, self.priv_key) = rsa.newkeys(1024)

    def setPubKey(self, key):
        n = key[0:315]
        e = key[315:len(key)]

        real_n = n.split('$')[0]
        real_e = e.split('$')[0]

        self.pub_key.__setattr__('n', int(real_n))
        self.pub_key.__setattr__('e', int(real_e))
        print(self.nick, self.pub_key)

    def getPubKey(self):
        return self.pub_key

    def getConn(self):
        return self.conn

    def getId(self):
        return self.id

    def getNick(self):
        return self.nick