import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.7"
        self.port = 8884
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    # get the starting position of the character
    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            # Once we connect, we need to send some info (validation token) immediately back to object connected to us
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()

        except socket.error as e:
            print(e)
