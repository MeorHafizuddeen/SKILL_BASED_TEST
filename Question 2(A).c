#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

// Macros definition for port number to use = 8443 and string size 1024
#define PORT 8443
#define MAX_BUFFER_SIZE 1024

// Function to generate random number
int gen_rand_num() {
    srand(time(NULL));
    return rand() % 900 + 100; // Generates a random number in the range 100 to 999
}

// Main function
int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    // Create a socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Error creating socket");
        return 1;
    }

    // Bind the socket to the server
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        return 1;
    }

    // Listen for client connection
    if (listen(server_socket, 1) == -1) {
        perror("Listening failed");
        return -1;
    }
    printf("Server waiting for incoming connections on port %d...\n", PORT);

    while (1) {
        // Accept incoming connection
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_addr_len);
        if (client_socket < 0) {
            perror("Accept failed");
            return 1;
        }

        printf("Client connected.\n");

        // Generate a random number
        int rand_num = gen_rand_num();
        char buffer[MAX_BUFFER_SIZE];
        snprintf(buffer, MAX_BUFFER_SIZE, "%d", rand_num);

        // Send the random number to the client
        send(client_socket, buffer, strlen(buffer), 0);
	printf("Random number sent to the client: %d \n", rand_num);

        // Close the client socket
        close(client_socket);
    }

    // Close the server socket
    close(server_socket);

    return 0;
}
