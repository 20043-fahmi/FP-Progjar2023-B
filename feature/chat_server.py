import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []
        self.server_running = False

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Chat server started on {}:{}".format(self.host, self.port))
        self.server_running = True

        while self.server_running:
            client_socket, client_address = self.server_socket.accept()
            print("New connection from {}:{}".format(client_address[0], client_address[1]))
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
            self.clients.append((client_socket, client_address))

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print("Received message: {}".format(message))
                    self.broadcast(message, client_socket)
                else:
                    self.remove_client(client_socket)
                    break
            except:
                self.remove_client(client_socket)
                break

    def remove_client(self, client_socket):
        client_socket.close()
        self.clients = [client for client in self.clients if client[0] != client_socket]

    def broadcast(self, message, sender_socket):
        for client_socket, _ in self.clients:
            if client_socket != sender_socket:
                client_socket.send(message.encode())

    def stop(self):
        self.server_running = False
        for client_socket, _ in self.clients:
            client_socket.close()
        self.server_socket.close()
        print("Chat server stopped.")

# Usage example
if __name__ == "__main__":
    server = ChatServer('localhost', 9999)
    server.start()
