import socket
import time
from Tkinter import *
from functools import partial
from random import randint


class TicTac(Frame):
    def __init__(self, master):
        self.tk = master
        self.is_server = False
        self.my_turn = False
        self.move = None
        self.buttons = {}
        for x, y in [(x, y) for x in range(3) for y in range(3)]:
            b = Button(self.tk, text="", command=partial(self.set_button_display, x, y), font=('Arial', 60), height=1,
                       width=3)
            self.buttons[(x, y)] = b
            b.grid(row=y, column=x)
        self.message = Label(self.tk, text="Waiting...", font=('Arial', 30))
        self.message.grid(row=3, column=0, columnspan=3, sticky=W)
        self.tk.update()
        self.tk.after(10, self.setup_connection)

    def set_button_display(self, x, y):
        if not self.my_turn:
            return
        print x, y
        self.my_turn = False
        self.move = (x, y)
        if self.is_server:
            self.message.config(text="Player 1.  Waiting.")
            self.buttons[(x, y)].config(text="X", state=DISABLED)
        else:
            self.message.config(text="Player 2. Waiting.")
            self.buttons[(x, y)].config(text="O", state=DISABLED)

    def opponent_move(self, move):
        if move == "aaa":
            return
        try:
            d = move.strip().split(",")
        except:
            print "ERROR!"
        print d
        if d:
            button = [int(x) for x in d]
            print button
            if self.is_server:
                self.buttons[tuple(button)].config(text="O", state=DISABLED)
            else:
                self.buttons[tuple(button)].config(text="X", state=DISABLED)
            self.my_turn = True
            self.message.config(text="your turn!")

    def setup_connection(self):
        self.serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        self.host = socket.gethostname()

        self.port = 9999

        # bind to the port
        try:
            self.serversocket.bind((self.host, self.port))
            self.is_server = True
        except:
            self.message.config(text="Player 2. Waiting for your turn.")
            print("I'm the client")
            while True:

                self.tk.update()
                try:
                    self.serversocket = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
                except:
                    print "socket in use"
                    #continue
                self.host = socket.gethostname()
                self.serversocket.connect((self.host, self.port))

                # Receive no more than 1024 bytes
                tm = self.serversocket.recv(1024)
                # print tm
                self.opponent_move(tm)
                if self.move:
                    print "MOVE!"
                    self.serversocket.send("{},{}".format(*self.move))
                    self.move = None
                else:
                    self.serversocket.send('aaa')
                self.serversocket.shutdown(socket.SHUT_RDWR)
                self.serversocket.close()

        else:
            # queue up to 5 requests
            self.serversocket.listen(50)
            self.my_turn = True

            while True:
                # establish a connection
                try:
                    # self.message.config(text="Player 1. Waiting for opponent...")
                    self.tk.update()
                    clientsocket, addr = self.serversocket.accept()
                    if self.my_turn:
                        self.message.config(text="Player 1.  Your turn!")
                    # print("Got a connection")
                    # currentTime = time.ctime(time.time()) + "\r\n"
                    if self.move:
                        print "MOVE!"
                        clientsocket.send("{},{}".format(*self.move))
                        self.move = None
                    else:
                        clientsocket.send("aaa")
                    b = clientsocket.recv(1024)
                    # print b
                    self.opponent_move(b)
                    clientsocket.close()
                except Exception as e:
                    print(e)


root = Tk()
myapp = TicTac(root)
myapp.mainloop()
