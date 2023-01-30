# TCP client side

import socket

# create a client side IPV4 socket (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to a server located at a given IP and port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345)) # we don't have to hardcode the address since the server is on the same machine as the client

# receive a message from the server...you must specify the max number of bytes to receive
message = client_socket.recv(1024) # may need to adjust the maximum number of bytes later
print(message.decode("utf-8"))

# close the client socket
client_socket.close()

