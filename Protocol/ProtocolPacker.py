import rsa

class ProtocolPacker(object):
    def __init__(self, id, nick, ip, port):
        self.id = str(id)
        self.nick = str(nick)
        self.ip = str(ip)
        self.port = str(port)
        self.handshake = '1' #1 = fazer handshake, 0 = nao fazer handshake
        (self.pub_key, self.priv_key) = rsa.newkeys(1024)
        (self.sv_pub_key, self.sv_priv_key) = rsa.newkeys(1024)
        print(self.nick, self.pub_key)

    def getId(self):
        return self.id

    def getNick(self):
        return self.nick

    def getIp(self):
        return self.ip

    def getPort(self):
        return self.port

    def setSvPubKey(self, key):
        real_key = key[3:len(key)]
        n = real_key[0:315]
        e = real_key[315:len(key)]

        real_n = n.split('$')[0]
        real_e = e.split('$')[0]

        self.sv_pub_key.__setattr__('n', int(real_n))
        self.sv_pub_key.__setattr__('e', int(real_e))
        print('servidor', self.sv_pub_key)

    '''
        tamanho do pacote:
            73bytes cabecalho +
            xbytes da msg, onde x = numero de chars da msg
    '''
    def newPacket(self, msg):
        packet = self.encodeId() + self.encodeNick() + self.encodeIp() + self.encodePort() + self.encodeHS() + msg.encode()
        return packet

    def newHandShakePacket(self):
        packet = self.encodeId() + self.encodeNick() + self.encodeIp() + self.encodePort() + self.encodeHS() + self.encodeN() + self.encodeE()
        self.handshake = '0'
        return packet

    def newSvHandShakePacket(self):
        packet = self.encodeId() + self.encodeNick() + self.encodeIp() + self.encodePort() + self.encodeHS() + '/s/'.encode() + self.encodeN() + self.encodeE()
        return packet

    def unpack(self, packet):
        strg = packet.decode()
        id = strg[0:3]
        nick = strg[3:18]
        ip = strg[18:33]
        port = strg[33:37]
        hs = strg[37:39]
        msg = strg[39:len(strg)]

        real_id = id.split('$')[0]
        real_nick = nick.split('$')[0]
        real_ip = ip.split('$')[0]
        real_port = port.split('$')[0]
        real_hs = hs.split('$')[0]

        partioned_msg = [real_id, real_nick, real_ip, real_port, real_hs, msg]
        return partioned_msg

    def encodeN(self):
        n = str(self.pub_key.__getattribute__('n'))
        if len(n) < 315:
            x = 315 - len(n)
            for i in range(0, x):
                n = n+'$'
        encodedN = n.encode()
        return encodedN

    def encodeE(self):
        e = str(self.pub_key.__getattribute__('e'))
        if len(e) < 6:
            x = 6 - len(e)
            for i in range(0, x):
                e = e+'$'
        encodedE = e.encode()
        return encodedE

    def encodeHS(self):
        if len(self.handshake) < 2:
            x = 2 - len(self.handshake)
            for i in range(0, x):
                self.handshake = self.handshake+'$'
        encodedHS = self.handshake.encode()
        return encodedHS

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