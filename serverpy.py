import socket

# Define the server address and port
server_address = ('10-hrsbeatsasha.ddns.net', 1234)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server started, listening on {}:{}'.format(*server_address))

while True:
    # Wait for a client to connect
    print('Waiting for a client to connect...')
    client_socket, client_address = server_socket.accept()
    print('Client connected:', client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print('Received from client:', data)

    # Process the data (you can add your logic here)

    # Send a response back to the client
    response = 'Hello, client!'
    client_socket.sendall(response.encode('utf-8'))
    print('Sent to client:', response)

    # Close the client socket
    client_socket.close()