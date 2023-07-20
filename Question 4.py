import socket
import threading	# Use thread to handle multiple clients
import random

# List of quotes in an array
# Use backslash to include quotation mark in output
quotes = [
    "\"If you can\'t be kind, be quiet.\"",
    "\"Don\'t prioritize those who take you as an option.\"",
    "\"Some people receives more flowers when they die than when they are alive.\"",
    "\"You never truly appreciate a moment until it became a memory.\"",
    "\"Trust is like a mirror. Once broken, it can never be fixed.\"",
]

# Function to handle a client
def handle_client(client_socket):
    # Send a random quote to the client
    random_quote = random.choice(quotes)
    client_socket.send(random_quote.encode())

    # Close the client socket
    client_socket.close()

# Server IP address, port and string size
server_address = '192.168.204.128'
server_port = 8888
buffer_size = 1024

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((server_address, server_port))

# Start listening for incoming connections
server_socket.listen(5)
print("Quote of the Day server is listening on port 8888...")

while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Create a new thread to handle the client request
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
