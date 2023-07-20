import socket

def get_quote():
    server_address = '192.168.204.128'  # Change this to the server IP address if needed
    server_port = 8888
    buffer_size = 1024

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))

        # Receive the quote from the server
        quote = client_socket.recv(buffer_size).decode()

        print(f"Random Quote of the Day:\n {quote}")

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and accessible.")
    except Exception as e:
        print("An error occurred:", str(e))

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    get_quote()
