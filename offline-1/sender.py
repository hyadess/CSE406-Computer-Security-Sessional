import socket
import encryptOp
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Two One Niee Two"
    client_socket.sendall(encryptOp.encryption(message).encode())

    # Receive the response from the server
    # data = client_socket.recv(1024)
    # print("Server response:", data.decode())
finally:
    # Clean up the connection
    client_socket.close()
