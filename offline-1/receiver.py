import socket
import decryptOp
import pickle
import AES_CBC
import AES_CTR
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on", server_address)

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print("Connected to", client_address)

    try:
        # Receive data from the client and send it back
        data = client_socket.recv(40960)
        received_bitstrings=pickle.loads(data)
        message=AES_CBC.CBC_decrypt(received_bitstrings)
        print(message)
        #client_socket.sendall(data)
    finally:
        # Clean up the connection
        client_socket.close()
