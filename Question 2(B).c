#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_IP "192.168.204.128"// Define macro IP address of server = 192.168.204.128
#define PORT 8443			// Define macro port number to use = 8443
#define MAX_BUFFER_SIZE 1024	// Define macro string size = 1024

int main() {
    int client_socket;
    struct sockaddr_in server_addr;
    char buffer[MAX_BUFFER_SIZE];

    // Create a socket
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket == -1) {
        perror("Error creating socket");
        return 1;
    }

    // Connect to the server
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);
    server_addr.sin_port = htons(PORT);
    if (connect(client_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        return 1;
    }
    printf("\nConnected to %s:%d\n", SERVER_IP, PORT);

    // Receive the random number from the server
    recv(client_socket, buffer, MAX_BUFFER_SIZE, 0);

    // Convert the received buffer to an integer (random number)
    int rand_num = atoi(buffer);

    printf("Received random number from the server: %d\n", rand_num);

    // Close the client socket
    close(client_socket);

    return 0;
} 
