import socket
import pickle
# pickle => allows to serialize objects => turn it into byte information -> send it over network -> decompose -> turn back into object

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.7"
        self.port = 8883
        self.addr = (self.server, self.port)
        self.p = self.connect()

    # get the starting position of the character
    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            # Once we connect, we need to decompose the object data
            return pickle.loads(self.client.recv(2048))          # load byte data
        except:
            pass

# get object => decompose the object and not the bytes => send it into byte information and decompose it on server side

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))

        except socket.error as e:
            print(e)
