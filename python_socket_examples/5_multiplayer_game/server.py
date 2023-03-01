# Online Multiplayer Game Server
import socket, threading, json, time

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# define socket constants to be used and ALTERED
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 54321

# define pygame constants to be used and ALTERED
ROOM_SIZE = 700 # game window size
PLAYER_SIZE = 20
ROUND_TIME = 45
FPS = 15
TOTAL_PLAYERS = 4

# room must be divisible by player size for correct gameplay, adjust as needed.
while ROOM_SIZE % PLAYER_SIZE != 0:
    PLAYER_SIZE += 1

# maximum number of players allowed is 4!
if TOTAL_PLAYERS > 4:
    TOTAL_PLAYERS = 4
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# define classes
class Connection():
    '''A socket connection class to be used as a server'''
    def __init__(self):
        '''Initialization of the Connection class'''
        self.encoder = 'utf-8'
        # the server will send a fixed-length header packet indicating the length of the message before sending
        self.header_length = 10 # means messages can be a max of 9,999,999,999 characters 

        # create a socket, bind, and listen
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST_IP, HOST_PORT))
        self.server_socket.listen()

class Player():
    """A class to store a connected client's player information"""
    def __init__(self, number):
        '''Initialization of the Player class'''
        pass

    def set_player_info(self, player_info):
        '''Set the player info to the given info from the client (coordinate & status flags)'''
        pass

    def reset_player(self):
        '''Reset player values for a new round on the server side'''
        pass

class Game():
    '''A class to handle all operations of gameplay'''
    def __init__(self, connection):
        '''Initialization of the Game class'''
        self.connection = connection
        self.player_count = 0
        self.player_objects = []
        self.player_sockets = []
        self.round_time = ROUND_TIME


    def connect_players(self):
        '''Connect ANY incoming player to the game'''
        # only accept players if the player count is less than total players
        while self.player_count < TOTAL_PLAYERS:
            # Accept incoming player socket connections
            player_socket, player_address = self.connection.server_socket.accept()

            # send the current game configuration values over to the client by converting the pygame constants from integers into strings
            # the header message packet has a fixed length of 10 which holds the header which tells the receiver the length of the message coming in
            # the header length can be no more than 10
            header = str(len(str(ROOM_SIZE)))
            while len(header) < self.connection.header_length: # append white space characters to the end of the header "3" -> "3         " (a length of 1 for instance to a length of 10)
                header += " "
            player_socket.send(header.encode(self.connection.encoder)) # encode & send the header message packet
            player_socket.send(str(ROOM_SIZE).encode(self.connection.encoder)) # encode & send the message (game config. or pygame constant)     header = str(len(str(ROOM_SIZE)))

            # header = str(len(str()))
            # while len(header) < self.connection.header_length: # append white space characters to the end of the header "3" -> "3         " (a length of 1 for instance to a length of 10)
            #     header += " "
            # player_socket.send(header.encode(self.connection.encoder)) # encode & send the header message packet
            # player_socket.send(ROOM_SIZE.encode(self.connection.encoder)) # encode & send the message (game config. or pygame constant)     header = str(len(str(ROUND_TABLE)))

            header = str(len(str(ROUND_TIME)))
            while len(header) < self.connection.header_length: # append white space characters to the end of the header "3" -> "3         " (a length of 1 for instance to a length of 10)
                header += " "
            player_socket.send(header.encode(self.connection.encoder)) # encode & send the header message packet
            player_socket.send(str(ROUND_TIME).encode(self.connection.encoder)) # encode & send the message (game config. or pygame constant)     header = str(len(str(ROUND_TIME)))

            header = str(len(str(FPS)))
            while len(header) < self.connection.header_length: # append white space characters to the end of the header "3" -> "3         " (a length of 1 for instance to a length of 10)
                header += " "
            player_socket.send(header.encode(self.connection.encoder)) # encode & send the header message packet
            player_socket.send(str(FPS).encode(self.connection.encoder)) # encode & send the message (game config. or pygame constant)     header = str(len(str(FPS))

            header = str(len(str(TOTAL_PLAYERS)))
            while len(header) < self.connection.header_length: # append white space characters to the end of the header "3" -> "3         " (a length of 1 for instance to a length of 10)
                header += " "
            player_socket.send(header.encode(self.connection.encoder)) # encode & send the header message packet
            player_socket.send(str(TOTAL_PLAYERS).encode(self.connection.encoder)) # encode & send the message (game config. or pygame constant)      header = str(len(str(TOTAL_PLAYERS))

            # create a new 'Player()' object for the connected client
            self.player_count += 1 # increment the # of players
            player = Player(self.player_count) # pass in the player's number as an attribute
            self.player_objects.append(player) # add player to the player object list
            self.player_sockets.append(player_socket) # add the player's socket to the player socket list
            print(f"New player joining from {player_address}...Total players: {self.player_count}") # the IP address of the player/client's computer

        # maximum num of players reached. No longer accepting new players
        print(f"{TOTAL_PLAYERS} players in game. No longer accepting new players...")




    def broadcast(self):
        '''Broadcast info to all players'''
        pass

    def ready_game(self, player, player_socket):
        '''Ready the game to be played for a SPECIFIC player'''
        pass

    def reset_game(self, player):
        '''Restart the game and wipe info for a SPECIFIC player'''
        pass

    def send_player_info(self, player, player_socket):
        '''Send specific info about this player to a GIVEN client'''
        pass

    def receive_pregame_player_info(self, player, player_socket):
        '''Receive specific info about THIS player pregame'''
        pass
    def receive_game_player_info(self, player, player_socket):
        '''Receive specific info about THIS player during the game'''
        pass
    def process_game_state(self, player, player_socket):
        '''Process the given player info and update the game's state'''
        pass
    def send_game_state(self, player_socket):
        '''Send the correct game state of ALL players to THIS given player'''
        pass

# start the server
my_connection = Connection()
my_game = Game(my_connection) # passing in our 'Connection()' class obj. 'my_connection' as the 'connection' attribute for 'Game()' class obj. 'my_game'

# Listen for incoming connections
print ("Server is listening for incoming connections...\n")
my_game.connect_players()
