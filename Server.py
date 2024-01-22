import socket
from Player import Player
import pickle
from _thread import *

server = "192.168.0.25"
port = 5555

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# If the port I have decided on was not free then the program would break
# and so I had to implement a try and expect when connecting.
try:
    Socket.bind((server,port))
except socket.error as error:
    str(error)

Socket.listen(2) #2 connections

# Using this to test the server is working
print("Server Started.")
print("Waiting for connection.")

# Game related data
players = [Player(100,100,50,50,(0,255,0)), Player(1240, 760, 50,50, (50,150,220))]

def threaded_client(connection:tuple, player, connectedPlayers):
    # Sends out the position of the player
    connection.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:
            # Recieves the position data for the player
            data = pickle.loads(connection.recv(2048))
            players[player] = data

            if not data:
                print("Disconnecting...")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending: ", reply)

            connection.sendall(pickle.dumps(reply))
        except:
            break
    
    print("Lost connection")
    connection.close()
    connectedPlayers[player] = False


connectedPlayers = {0: False,
                    1: False}

currentPlayer = -1
# Main server loop
while True:
    connection, addr = Socket.accept()
    print("Connected to: ", addr)

    #Assigns whether the player is player 1 or 2 (0 or 1)
    if not connectedPlayers[0]:
        connectedPlayers[0] = True
        currentPlayer = 0
    elif not connectedPlayers[1]:
        connectedPlayers[1] = True
        currentPlayer = 1

    start_new_thread(threaded_client, (connection, currentPlayer, connectedPlayers))   