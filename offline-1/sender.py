import socket
import encryptOp
import pickle
import AES_CBC
import AES_CTR
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "lets see what happens!!! wow, it is done!!!!....worked very fine..."
    msgArray=AES_CBC.CBC_encrypt(message)
    serialized=pickle.dumps(msgArray)
    client_socket.sendall(serialized)

    # Receive the response from the server
    # data = client_socket.recv(1024)
    # print("Server response:", data.decode())
finally:
    # Clean up the connection
    client_socket.close()
