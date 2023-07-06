import tkinter as tk
import socket
import threading
from tkinter.scrolledtext import ScrolledText


class ChatPage(tk.Frame):
    def __init__(self, parent, client_socket):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.client_socket = client_socket
        self.create_widgets()

    def create_widgets(self):
        # Chat display area
        self.chat_display = ScrolledText(self, height=15, state='disabled')
        self.chat_display.pack(fill='both', expand=True)

        # User input area
        self.input_frame = tk.Frame(self, background='white')
        self.input_frame.pack(fill='x')

        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side='left', fill='x', expand=True)
        self.input_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            self.input_frame, text='Send', command=self.send_message)
        self.send_button.pack(side='right')

    def send_message(self, event=None):
        message = self.input_entry.get()
        if message:
            self.display_message("You: " + message)
            self.client_socket.send(message.encode())
            self.input_entry.delete(0, 'end')

    def display_message(self, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert('end', message + '\n')
        self.chat_display.configure(state='disabled')
        self.chat_display.see('end')


class ChatClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        self.nickname = self.set_nickname()

    def set_nickname(self):
        root = tk.Tk()
        root.withdraw()
        nickname = tk.simpledialog.askstring(
            "Nickname", "Please enter your nickname:")
        self.client_socket.send(nickname.encode())
        return nickname

    def receive_messages(self, chat_page, nickname):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                chat_page.display_message({self.nickname} + ": " + message)
            except:
                print("Error receiving messages")
                self.client_socket.close()
                break

    def start(self):
        root = tk.Tk()
        root.title("Chat Client")
        chat_page = ChatPage(root, self.client_socket)
        chat_page.pack()

        receive_thread = threading.Thread(
            target=self.receive_messages, args=(chat_page,))
        receive_thread.start()


if __name__ == "__main__":
    chat_client = ChatClient()
    chat_client.start()
    tk.mainloop()
