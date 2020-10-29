# Use sockets and threading to handle connections to server
# Set up a socket => allow connections to come into our server on a certain port
# First run server and then can run multiple client script on it

import socket
from _thread import *
from game import Game
import pickle

server = "192.168.1.7"      # Computer's ipv4 address
port = 8847                 # port to connect to and from

# Create a socket => set up a connection or using a port on our server/port that look for certain connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server and port to the socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Open up the port => start connecting to it and have multiple clients connect to it
# s.listen() => allow unlimited connections to happen
# s.listen(n) => allow n connections to happen
s.listen()

print("Waiting for connection, Server Started")

connected = set()                   # Store IP addresses of connected clients
games = {}                          # store the games, key => id, value => game object
idCount = 0                         # keep track of current id so that two games dont have same id


# Run in the background, dont have to wait for it to finish execution
# Want it to continuously run while our client is still connected
def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))               # Encode the player which will be decoded by the network afterwards

    reply = ""

    # Send string data from client to our server
    # 3 options => get(get the game from server) / reset(reset the game when finished) / move (rock/paper/scissor)
    while True:
        try:
            data = conn.recv(4096).decode()             # too much information may be possible, constantly receive string data from client

            # Check if the game still exists
            # If one of clients disconnects from the game => delete that game
            if gameId in games:
                game = games[gameId]

                # Check if the client is sending reset/get/remove
                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()

                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    # If we break out of the while loop - (game no longer exists, something wrong with getting data)
    print("Lost Connection")

    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass

    idCount-=1
    conn.close()

# Continuously look for connections and see if something is connected
while True:
    # conn => object, addr => ip address
    conn, addr = s.accept()      # Accept any incoming connections and store the connection and the address
    print("Connected to:", addr)

    idCount+=1                      # How many people connected to the server

    # Current player
    p = 0
    gameId = (idCount-1)//2             # 10 people connected to server => 5 games, 11th person => join in a new game

    # If we dont have a pair for the new player i.e. odd amount of players
    if idCount%2==1:
        games[gameId] = Game(gameId)        # Add a new game in the games dictionary
        print("Creating a new game.....")
    else:
        games[gameId].ready = True          # We have 3 player and one more person joins => have to join the already made game
        p = 1

    # Thread => process running in the background
    start_new_thread(threaded_client, (conn, p, gameId))
