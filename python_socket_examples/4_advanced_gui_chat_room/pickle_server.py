# pickle server
import socket, pickle

# let's create a regular old list
unpickled_list = ['dill', 'bread and butter', 'half-sour']
print(unpickled_list)
print(type(unpickled_list)) # list obj.

# try to encode the list using .encode() (Doesn't work b/c not a string object)
# trial_list = unpickled_list.encode()
# print(trial_list)
# print(type(trial_list)

# now let's encode by pickling the list
pickled_list = pickle.dumps(unpickled_list) # encode the unpickled list
print(pickled_list)
print(type(pickled_list)) # bytes obj.

# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
server_socket.listen()


# listen forever to accept ANY connection
while True:
    client_socket, client_address = server_socket.accept()
    print(f"connected to {client_address}!\n")

    # send the encoded pickled list...THIS IS ALREADY ENCODED
    client_socket.send(pickled_list)

    # close the socket
    server_socket.close()