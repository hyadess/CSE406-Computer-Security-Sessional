import socket
import decryptOp
import pickle
import AES_CBC
import AES_CTR
import sender_receiver_helper
import ECDH_key_production
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
print("Server is listening on", server_address)


def keyExchange(communicateSocket):
 

    gx=sender_receiver_helper.receiveNumber(communicateSocket)
    gy=sender_receiver_helper.receiveNumber(communicateSocket)
    print("point G is received")
    
    a=sender_receiver_helper.receiveNumber(communicateSocket)
    b=sender_receiver_helper.receiveNumber(communicateSocket)
    print(" parameters a and b are received")
    p=sender_receiver_helper.receiveNumber(communicateSocket)
    print("prime p is received")
    print(gx,gy,a,b,p)
  


    privateKey,publicKey=ECDH_key_production.generatePublicPrivatePair(gx,gy,a,p)

    receiverKeyX=sender_receiver_helper.receiveNumber(communicateSocket)
    receiverKeyY=sender_receiver_helper.receiveNumber(communicateSocket)
    print("public key point is recieved from sender")
    print(receiverKeyX,receiverKeyY)


    publicKeyX,publicKeyY=publicKey
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyX)
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyY)
    print("public key point is sent to sender")
    print(publicKey)
    
    sharedKey=ECDH_key_production.generateSharedKey(privateKey,(receiverKeyX,receiverKeyY),a,p)
    print(sharedKey)







while True:
    print("Waiting for a connection...")
    communicateSocket, client_address = server_socket.accept()
    print("Connected to", client_address)

    try:
        #keyExchange(communicateSocket)
        #print("done")
        received_bitstrings=sender_receiver_helper.receiveBitstrings(communicateSocket)


        start=time.time()
        #message=AES_CBC.CBC_decrypt(received_bitstrings)
        message=AES_CTR.CTR_decrypt(received_bitstrings)
        end=time.time()
        print("time for decryption: ",(end-start)*1000,"ms")

        print("recovered message:",message)
        #communicateSocket.sendall(data)
    finally:
        # Clean up the connection
        communicateSocket.close()
