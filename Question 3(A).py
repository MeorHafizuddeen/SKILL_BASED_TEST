import socket

# Function to convert pressure unit from bar to atm
def conv_bar_to_atm(bar):
    return bar * 0.986923

server_address = '192.168.204.128'  	# Server IP address = 192.168.204.128
server_port = 8443			# Port to use = 8443
buffer_size = 1024			# Maximum string size = 1024

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to server address and choosen port
server_socket.bind((server_address, server_port))

# Listening for incoming connections
server_socket.listen(1)
print("Server is waiting for connections...")

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    # Receive pressure value from the client
    bar = client_socket.recv(buffer_size).decode()
    bar = float(bar)

    # Convert pressure to atmosphere-standard
    atm = conv_bar_to_atm(bar)

    # Send the converted value back to the client
    client_socket.send(str(atm).encode())

    # Close the connection with the client
    client_socket.close()
