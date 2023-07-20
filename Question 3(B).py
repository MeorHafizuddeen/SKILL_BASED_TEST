import socket

server_address = '192.168.204.128'  	# Server IP address = 192.168.204.128
server_port = 8443			# Port to use = 8443
buffer_size = 1024			# Maximum string size = 1024

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((server_address, server_port))

    # Get user input for pressure in bar
    bar = float(input("Enter pressure in bar: "))

    # Send pressure value to the server
    client_socket.send(str(bar).encode())

    # Receive the converted pressure value (atmosphere-standard) from the server
    atm = client_socket.recv(buffer_size).decode()

    print(f"Pressure in atmosphere-standard: {atm} atm")

except ConnectionRefusedError:
    print("Connection refused. Make sure the server is running and accessible.")
except Exception as e:
    print("An error occurred:", str(e))

# Close the client socket
client_socket.close()
