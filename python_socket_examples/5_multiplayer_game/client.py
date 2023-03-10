# Online Multiplayer Game Client
import pygame, socket, threading, json

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# define_IP should be of the form '192.168.1' or other addresses
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 54321
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# define classes
class Connection():
    '''A socket connection class for players to connect to a server'''
    def __init__(self):
        """Initialization for the Connection class"""
        self.encoder = "utf-8"
        self.header_length = 10 # means messages can be a max of 9,999,999,999 characters or bytes

        # create a socket and connect
        self.player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player_socket.connect((DEST_IP, DEST_PORT))
class Player():
    '''A player class the client can control'''
    # take in 'connection' as an attribute as the player has to connect to the server to receive all the info about its setup
    def __init__(self, connection):
        pass

    def set_player_info(self, player_info):
        """Set the player info to the given info from the server"""
        # player_info attribute will be a dictionary with updates about the player's coordinates and status flags
        pass
    def update(self):
        '''Update the player by changing their coordinates in the game'''
        # gets called for every iteration of the game loop
        pass
    def reset_player(self):
        '''Reset player values for a new round on the client side'''
        pass

class Game():
    '''A game class to handle all operations of gameplay'''
    # when the client connects to the server, the server will send over the total # of players for the 'total_players' attribute
    def __init__(self, connection, player, total_players):
        '''Initialization of the Game class'''
        pass
    def ready_game(self):
        '''Ready the game to be played'''
        pass
    def start_game(self):
        '''Start the game'''
        pass
    def reset_game(self):
        '''Reset the game to be played'''
        pass
    def send_player_info(self):
        '''Send specific info about this player to the server'''
        # the player will update on the client side & this info will be sent to the server
        pass
    def receive_player_info(self):
        '''Receive specific info about this player from the server'''
        # the server will process the player's info and send it back for client to receive
        pass
    def receive_pregame_state(self):
        '''Receive ALL information about ALL players from the server before the game starts'''
        pass
    def receive_game_state(self):
        '''Receive ALL info about ALL players from the server during the game'''
        pass
    def process_game_state(self):
        '''Process the game state to update scores, winning player, time, etc.'''
        # make appropriate changes on each individual client
        pass

    # Pygame functions
    def update(self):
        "Update the game"
        pass

    def draw(self):
        '''Draw the game & all game assets to the window'''
        pass 

# create a connection and get game window information from the server
# the server will determine Pygame constants (e.g. room size, player size, round time, FPS, total players) & send this info to the connected client
my_connection = Connection()
packet_size = my_connection.player_socket.recv(my_connection.header_length).decode(my_connection.encoder) # receive header message packet from server as a string with a bytesize of 10 or 10 characters so the # '3' with nine " "'s
room_size = int(my_connection.player_socket.recv(int(packet_size)).decode(my_connection.encoder)) # packet size is now the integer 3 instead of string "3" with nine " " 's # everytime we write 'my_connection.player_socket.recv()' we receive the next message the server sends us
packet_size = my_connection.player_socket.recv(my_connection.header_length).decode(my_connection.encoder) # receive header message packet from server as a string with a bytesize of 10 or 10 characters so the # '3' with nine " "'s
round_time = int(my_connection.player_socket.recv(int(packet_size)).decode(my_connection.encoder)) # packet size is now the integer 3 instead of string "3" with nine " " 's # everytime we write 'my_connection.player_socket.recv()' we receive the next message the server sends us
packet_size = my_connection.player_socket.recv(my_connection.header_length).decode(my_connection.encoder) # receive header message packet from server as a string with a bytesize of 10 or 10 characters so the # '3' with nine " "'s
fps = int(my_connection.player_socket.recv(int(packet_size)).decode(my_connection.encoder)) # packet size is now the integer 3 instead of string "3" with nine " " 's # everytime we write 'my_connection.player_socket.recv()' we receive the next message the server sends us
packet_size = my_connection.player_socket.recv(my_connection.header_length).decode(my_connection.encoder) # receive header message packet from server as a string with a bytesize of 10 or 10 characters so the # '3' with nine " "'s
total_players = int(my_connection.player_socket.recv(int(packet_size)).decode(my_connection.encoder)) # packet size is now the integer 3 instead of string "3" with nine " " 's # everytime we write 'my_connection.player_socket.recv()' we receive the next message the server sends us




# Initialize pygame
pygame.init()

# set game constants
WINDOW_WIDTH = room_size # game window size
WINDOW_HEIGHT = room_size # game window size
ROUND_TIME = round_time
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAGENTA = (155, 0, 155)
FPS = fps # main game loop cannot run more than 'fps' frames per second
clock = pygame.time.Clock()
font = pygame.font.SysFont('gabriola', 28)

# create a game window
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Color Collide~~")

# create player & game objects
my_player = Player(my_connection)
my_game = Game(my_connection, my_player, total_players)

# the main game loop
running = True
while running:
    # check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the surface
    display_surface.fill(BLACK)

    # update and draw classes on the black canvas
    my_player.update() # don't have 'draw()' method for 'Player()' class because 'Player()' class obj. is an asset of the game since it's passed into the 'Game()' class
    my_game.update()
    my_game.draw()

    # update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)







