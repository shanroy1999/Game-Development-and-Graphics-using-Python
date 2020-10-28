# Use sockets and threading to handle connections to server
# Set up a socket => allow connections to come into our server on a certain port
# First run server and then can run multiple client script on it

import socket
from _thread import *
import sys
from player import Player
import pickle

server = "192.168.1.7"      # Computer's ipv4 address
port = 8883                 # port to connect to and from

# Create a socket => set up a connection or using a port on our server/port that look for certain connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server and port to the socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Open up the port => start connecting to it and have multiple clients connect to it
s.listen(2)
# s.listen() => allow unlimited connections to happen
# s.listen(n) => allow n connections to happen

print("Waiting for connection, Server Started")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 255, 0))]

# Run in the background, dont have to wait for it to finish execution
# Want it to continuously run while our client is still connected
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))          # send the player object => send all the info rather than just the position
    reply = ""
    while True:
        # try to receive some kind of data
        try:
            data = pickle.loads(conn.recv(2048))       # amount of data(2048 bits) we will receive, larger the size => longer to receive/send info
            # We receive encoded info => needs to be decoded to read
            # read_pos => converts the data into a readable tuple

            # Update the current player's position
            players[player] = data

            # If we are unable to receive any information from the client
            if not data:
                print("Disconnected")
                break
            else:
                if player==1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ",data)
                print("Sending: ",reply)

            # Encode the information string 'reply' into a bytes object => need to be decoded again from client side to read info
            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost Connection")
    conn.close()

# Keep track of which player we are using
currentPlayer = 0

# Continuously look for connections and see if something is connected
while True:
    conn, addr = s.accept()      # Accept any incoming connections and store the connection and the address
    # conn => object, addr => ip address
    print("Connected to:", addr)

    # Thread => process running in the background
    start_new_thread(threaded_client, (conn, currentPlayer))

    currentPlayer+=1        # Every time we accept a new connection we will add 1 to currentPlayer
