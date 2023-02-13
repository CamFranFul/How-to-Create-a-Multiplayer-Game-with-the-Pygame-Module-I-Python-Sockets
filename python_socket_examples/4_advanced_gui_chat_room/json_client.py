# client side Json
import socket, json

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# receive the encoded json object (string) form the server...do we have to decode???? (apparently you don't have to, 'json.loads()' can directly convert from a bytes object to a the original Python message dictionary object)
message_json = client_socket.recv(1024)
print(message_json)
print(type(message_json))

# turn the bytes object or string object (if you already decoded it) back into a dict using json
# the json.loads() method can kill 2 birds with 1 stone: it can de-serialize a bytes obj. such as the encoded string containing a json obj. into the original Python message obj. or it can just solely go from a bytes obj. containing the encoded string json obj. to a string or just from the json obj. string to the original Python message obj.
message_packet = json.loads(message_json)
print(message_packet)
print(type(message_packet))

# our new object is in fact a dict
print(message_packet['message'])
for (key, value) in message_packet.items():
    print(f"{key}:{value}")

# close the socket
client_socket.close()
