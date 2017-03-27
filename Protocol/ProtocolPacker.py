class ProtocolPacker(object):
    def __init__(self, id, nick, ip, port):
        self.id = str(id)
        self.nick = str(nick)
        self.ip = str(ip)
        self.port = str(port)

    def getId(self):
        return self.id

    def getNick(self):
        return self.nick

    def getIp(self):
        return self.ip

    def getPort(self):
        return self.port

    '''
        tamanho do pacote:
            70bytes cabecalho +
            xbytes da msg, onde x = numero de chars da msg
    '''
    def newPacket(self, msg):
        packet = self.encodeId() + self.encodeNick() + self.encodeIp() + self.encodePort() + msg.encode()
        return packet

    def unpack(self, packet):
        strg = packet.decode()
        id = strg[0:3]
        nick = strg[3:18]
        ip = strg[18:33]
        port = strg[33:37]
        msg = strg[37:len(strg)]

        real_id = id.split('$')[0]
        real_nick = nick.split('$')[0]
        real_ip = ip.split('$')[0]
        real_port = port.split('$')[0]

        partioned_msg = [real_id, real_nick, real_ip, real_port, msg]
        return partioned_msg

    def encodeId(self):
        if len(self.id) < 3:
            x = 3 - len(self.id)
            for i in range(0, x):
                self.id = self.id+'$'
        encodedId = self.id.encode()
        return encodedId

    def encodeIp(self):
        if len(self.ip) < 15:
            x = 15 - len(self.ip)
            for i in range(0, x):
                self.ip = self.ip+'$'
        encodedIp = self.ip.encode()
        return encodedIp

    def encodePort(self):
        if len(self.port) < 4:
            x = 4 - len(self.port)
            for i in range (0, x):
                self.port = self.port+'$'
        encodedPort = self.port.encode()
        return encodedPort

    def encodeNick(self):
        if len(self.nick) < 15:
            x = 15 - len(self.nick)
            for i in range (0, x):
                self.nick = self.nick+'$'
        encodedNick = self.nick.encode()
        return encodedNick