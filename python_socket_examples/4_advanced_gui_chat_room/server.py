# server side for GUI chat room (admin)
import tkinter, socket, threading, json
from tkinter import DISABLED, VERTICAL

# define window
root = tkinter.Tk()
root.title("Chat Server")
root.iconbitmap("message_icon.png")
root.geometry('600x600')
root.resizable(0,0) # user not able to resize window

# define fonts and colors
my_font = ('SimSun', 14)
black = "#010101"
light_green = "#1fc742"
root.config(bg=black)

# define functions



# define GUI layout
# create frames
connection_frame = tkinter.Frame(root, bg=black)
history_frame = tkinter.Frame(root, bg=black)
client_frame = tkinter.Frame(root, bg=black)
message_frame = tkinter.Frame(root, bg=black)
admin_frame = tkinter.Frame(root, bg=black)

# I guess the order that you define these baraibles with ".pack()" is the order that they appear on the root window when the program is run
connection_frame.pack(pady=5)
history_frame.pack()
client_frame.pack(pady=5)
message_frame.pack()
admin_frame.pack()


# connection frame layout
port_label = tkinter.Label(connection_frame, text="Port Number: ", font=my_font, bg=black, fg=light_green)
port_entry = tkinter.Entry(connection_frame, width=10, borderwidth=3, font=my_font)
start_button = tkinter.Button(connection_frame, text="Start Server", borderwidth=5, width=15, font=my_font, bg=light_green)
end_button = tkinter.Button(connection_frame, text="End Server", borderwidth=5, width=15, font=my_font, bg=light_green, state=DISABLED)


port_label.grid(row=0, column=0, padx=2, pady=10)
port_entry.grid(row=0, column=1, padx=2, pady=10)
start_button.grid(row=0, column=2, padx=5, pady=10)
end_button.grid(row=0, column=3, padx=5, pady=10)

# history frame layout
history_scrollbar = tkinter.Scrollbar(history_frame, orient=VERTICAL) # define scroll bar to scroll through sent messages
history_listbox = tkinter.Listbox(history_frame, height=10, width=55, borderwidth=3, bg=black, fg=light_green, yscrollcommand=history_scrollbar.set) # I guess don't have to put parenthesis when call functions in class attributes; the container that holds the sent messages
history_scrollbar.config(command=history_listbox.yview) # to synchronize the scroll bar with the listbox so that the scroll bar changes the vertical view of the listbox

# place the widgets onto the history frame via the grid system
history_listbox.grid(row=0, column=0) # don't know why the outline of the listbox is not showing up like in the tutorial
history_scrollbar.grid(row=0, column=1, sticky="NS") # sticky='NS' expands the scroll bar north and south (stretches it in both directions)


# run the root window's mainloop()
root.mainloop() # calls the functions of the Tk() class