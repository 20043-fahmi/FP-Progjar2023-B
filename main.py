import tkinter as tk
import socket
import threading
from feature.chat import ChatPage
from feature.game import Game


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main Window")

        self.game = Game(self)
        self.chat = ChatPage(self)

        self.game.grid(row=0, column=0, padx = 20, pady = 20)
        self.chat.grid(row=0, column=1, padx = 20, pady = 20)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
