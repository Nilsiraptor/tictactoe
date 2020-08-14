# imports ----------------------------------------------------------------------
from tkinter import *
from socket import *
from PIL import Image, ImageTk
import publicip
from contextlib import redirect_stdout
import io

# game variables ---------------------------------------------------------------
ingame = False
player = None
board_state = [0]*9

# connection variables ---------------------------------------------------------
HEADER_SIZE = 2
client_socket = None
server_socket = None
SERVER = FALSE
PORT = 25565
connected = False

# functions --------------------------------------------------------------------
def draw_board(canvas):
    global board_state
    #root.update()
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    canvas.create_line(width//3, 0.03*height, width//3, 0.97*height, capstyle="round", width=12)
    canvas.create_line(2*width//3, 0.03*height, 2*width//3, 0.97*height, capstyle="round", width=12)

    canvas.create_line(0.03*width, height//3, 0.97*width, height//3, capstyle="round", width=12)
    canvas.create_line(0.03*width, 2*height//3, 0.97*width, 2*height//3, capstyle="round", width=12)

    for i in range(3):
        for j in range(3):
            if board_state[i+j*3] == 1:
                draw_cross(canvas, i, j)
            elif board_state[i+j*3] == 2:
                draw_circle(canvas, i, j)

def draw_cross(canvas, i, j):
    #root.update()
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    x = i*width//3 + width//6
    y = j*height//3 + height//6
    canvas.create_line(x-width//8, y-height//8, x+width//8, y+height//8, capstyle="round", width=12)
    canvas.create_line(x+width//8, y-height//8, x-width//8, y+height//8, capstyle="round", width=12)

def draw_circle(canvas, i, j):
    #root.update()
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    x = i*width//3 + width//6
    y = j*height//3 + height//6
    canvas.create_oval(x-width//8, y-height//8, x+width//8, y+height//8, width=12)

def resize(event, canvas):
    canvas.delete("all")
    draw_board(canvas)

def new_game():
    pass

def connect():
    pass

def start_server():
    global server_socket, SERVER, IP

    if not SERVER:
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind(("0.0.0.0", PORT))
        server_socket.listen()

        status_bar.config(text="Server is now online")
        f = io.StringIO()
        with redirect_stdout(f):
            publicip.get()

        IP = f.getvalue().strip()

        ip_text.config(state="normal")
        ip_text.insert(0, IP)
        ip_text.config(state="readonly")
        ip_label.pack()

        host_button.config(text="Stop Server")
        start_button.config(state="normal")

        SERVER = True
    else:
        pass

def clicked(e):
    pass

# create window ----------------------------------------------------------------
root = Tk()
root.title("TicTacToe")
root.iconbitmap("Bilder/tictactoe.ico")

# add menu bar -----------------------------------------------------------------
menu = Menu(root)
root.config(menu=menu)

help_menu = Menu(menu)
menu.add_cascade(label="Hilfe", menu=help_menu)

# create window layout ---------------------------------------------------------
status_bar = Label(root, text="Status", anchor="e", relief="sunken")
status_bar.pack(side="bottom", fill="x")

canvas = Canvas(root, width=400, height=400)
canvas.pack(side="left", expand=True, fill="both")

right_frame = Frame(root, width=233)
right_frame.pack(side="right", fill="y")

ip_frame = Frame(right_frame, relief="ridge", bd=2)
ip_frame.pack(fill="x")

join_padding = Frame(right_frame, relief="ridge", bd=2)
join_padding.pack(fill="both", expand=True)

join_frame = Frame(join_padding)
join_frame.pack(fill="both", padx=20, pady=20)

host_padding = Frame(right_frame, relief="ridge", bd=2)
host_padding.pack(fill="both", expand=True)

host_frame = Frame(host_padding)
host_frame.pack(fill="both", padx=20, pady=20)

ip_text = Entry(ip_frame, justify="left", state="readonly", relief="flat")
ip_text.pack(side="right", fill="x")

ip_label = Label(ip_frame, text="Deine IP-Adresse:", anchor="e")
ip_label.pack(side="left", fill="x")
ip_label.pack_forget()

join_button = Button(join_frame, text="Beitreten", command=connect)
join_button.pack(side="bottom", fill="both")

join_entry = Entry(join_frame, justify="left")
join_entry.pack(side="right", fill="x")

join_label = Label(join_frame, text="IP-Adresse:", anchor="e")
join_label.pack(side="left", fill="x")

host_button = Button(host_frame, text="Host Server", command=start_server)
host_button.pack(fill="both")

start_button = Button(host_frame, text="Neues Spiel", command=new_game, state="disabled")
start_button.pack(fill="both")

# settings ---------------------------------------------------------------------
# set minimum window size
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

# bind redraw to resize event
root.bind("<Configure>", lambda e: resize(e, canvas))
canvas.bind("<Button-1>", lambda e: clicked(e))

# graphic setup ----------------------------------------------------------------
draw_board(canvas)

# start main loop --------------------------------------------------------------
root.mainloop()
