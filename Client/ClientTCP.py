import socket
import itertools
import threading
from tkinter import *
from Protocol.ProtocolPacker import ProtocolPacker


class ClientTCP:

    #TO DO: AO FECHAR CONEXAO PELO HOST, SERVIDOR DEVE ATUALIZAR A LISTA DE CLIENTES CONECTADOS

    id = itertools.count() #contador estatico //NAO TA FUNCIONANDO O CONTADOR :(
    def __init__(self, ip, porta, nick, master):
        self.master = master
        self.left_frame = Frame(self.master, width=200)
        self.left_frame.pack(side=LEFT)

        self.right_frame = Frame(self.master, width=300)
        self.right_frame.pack(side=RIGHT)

        #configurando frame da esquerda
        self.connected_clients = Listbox(self.left_frame, height=22)
        self.connected_clients.pack()

        #configurando frame da direita
        self.chat_text = Text(self.right_frame, width=37, height=20)
        self.chat_text.grid(row=0, column=0, columnspan=3, rowspan=2, padx=5, pady=5, sticky=W + E + N + S)
        self.chat_text.configure(state='disabled')

        self.msg_entry = Entry(self.right_frame, width=52)
        self.msg_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.send_button = Button(self.right_frame, text='Send', width=4, height=1, command=self.buttonClick)
        self.send_button.grid(row=2, column=3, padx=5, pady=5)

        self.id = next(self.id) #proximo id
        self.nick = nick
        self.ip = ip
        self.port = porta

        self.packer = ProtocolPacker(self.id, self.nick, self.ip, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket ipv4 tcp

        self.online = True
        self.handShake()

        recv_pkt = threading.Thread(target=self.receivePacket)
        recv_pkt.daemon = True
        recv_pkt.start()

    def buttonClick(self):
        sending = self.msg_entry.get()
        self.chat_text.configure(state='normal')
        self.chat_text.insert(END, 'Voce' + ': ' + sending + '\n')
        self.chat_text.configure(state='disabled')
        self.sendPacket(sending)

    def handShake(self):
        self.socket.connect((self.ip, self.port))
        self.sendPacket('handshake')

    def closeConnection(self):
        self.sendPacket('/e/')
        self.master.destroy()
        sys.exit()
        self.socket.close()

    def sendPacket(self, msg):
        if self.online:
            self.socket.sendall(self.packer.newPacket(msg))
        else:
            self.closeConnection()

    def receivePacket(self):
        while self.online:
            try:
                packet = self.socket.recv(1024)
                if packet:
                    incNick = self.packer.unpack(packet)[1]
                    incMsg = self.packer.unpack(packet)[4]
                    begin_msg = incMsg[0:3]
                    if begin_msg == '/d/':
                        self.privateMsg(incNick, incMsg)
                    elif begin_msg == '/r/':
                        self.removedMsg()
                    elif begin_msg == '/c/':
                        self.clientConnectedMsg(incMsg)
                    else:
                        self.chat_text.configure(state='normal')
                        self.chat_text.insert(END, incNick + ': ' + incMsg + '\n')
                        self.chat_text.configure(state='disabled')
                        print(incNick, ": ", incMsg)
            except:
                pass
        if not self.online:
            self.master.destroy()
            sys.exit()

    def privateMsg(self,incNick, incMsg):
        msg = incMsg.split('~')[1]
        msg = '/Private/' + msg
        self.chat_text.configure(state='normal')
        self.chat_text.insert(END, incNick + ': ' + msg + '\n')
        self.chat_text.configure(state='disabled')
        print(incNick, ': ', msg)

    def removedMsg(self):
        self.chat_text.configure(state='normal')
        self.chat_text.insert(END, 'Voce foi removido do servidor pelo ADM' + '\n')
        self.chat_text.configure(state='disabled')
        print('Voce foi removido do servidor pelo ADM')
        self.online = False

    def clientConnectedMsg(self, incMsg):
        msg = incMsg[3:len(incMsg)]
        nameList = msg.split('~')
        del nameList[-1]

        self.connected_clients.delete(0, END)
        for user in nameList:
            self.connected_clients.insert(END, user)