# Tkinter introduction
import tkinter
from tkinter import BOTH

# define window
root = tkinter.Tk()
root.title("Let's Chat")
root.iconbitmap('blue_talk.png')
root.geometry('400x600')
root.resizable(0,0)

# define colors
root_color = "#535657"
input_color = "#4f646f"
output_color = "#dee7e7"
root.config(bg=root_color)

# define functions


# define GUI layout
# define frames (that are placed on the root window)
input_frame = tkinter.LabelFrame(root, bg=input_color) # bg stands for background
output_frame = tkinter.LabelFrame(root, bg=output_color) # bg stands for background
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

# define widgets (that are placed on the frames)
message_entry = tkinter.Entry(input_frame, text = "Enter a message", width =30)
send_button = tkinter.Button(input_frame, text="Send")
message_entry.grid(row=0, column=0, padx=10, pady=10)
send_button.grid(row=0, column=1, padx=10, pady=10) # did not include "ipadx=20, ipady=5" as the button gets cut off


# run the loop window's mainloop()
root.mainloop()


