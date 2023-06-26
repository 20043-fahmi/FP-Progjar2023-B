import socket
import threading


def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Received message from {address}: {message}")
        # Kirim pesan kepada client yang lain
        send_to_other_clients(message, client_socket)

    # Jika keluar dari perulangan, tutup socket klien
    print(f"Client disconnected: {address}")
    client_sockets.remove(client_socket)
    client_socket.close()


def send_to_other_clients(message, sender_socket):
    for client_socket in client_sockets:
        if client_socket != sender_socket:
            client_socket.send(message.encode())


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)
    print("Server started. Waiting for clients...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Client connected from {address}")
        client_sockets.append(client_socket)
        threading.Thread(target=handle_client, args=(
            client_socket, address)).start()


client_sockets = []

start_server()
