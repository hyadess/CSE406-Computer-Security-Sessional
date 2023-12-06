import socket

import importlib
decryptOp=importlib.import_module("1905064_decryptOp")
AES_CBC=importlib.import_module("1905064_AES_CBC")
AES_CTR=importlib.import_module("1905064_AES_CTR")
sender_receiver_helper=importlib.import_module("1905064_sender_receiver_helper")
ECDH_key_production=importlib.import_module("1905064_ECDH_key_production")
keyGeneration=importlib.import_module("1905064_keyGeneration")
bitStringOp=importlib.import_module("1905064_bitStringOp")
import pickle


import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
print("Server is listening on", server_address)


def keyExchange(communicateSocket):
 

    gx=sender_receiver_helper.receiveNumber(communicateSocket)
    gy=sender_receiver_helper.receiveNumber(communicateSocket)
    #print("point G is received")
    
    a=sender_receiver_helper.receiveNumber(communicateSocket)
    b=sender_receiver_helper.receiveNumber(communicateSocket)
    #print(" parameters a and b are received")
    p=sender_receiver_helper.receiveNumber(communicateSocket)
    #print("prime p is received")
    #print(gx,gy,a,b,p)
  


    privateKey,publicKey=ECDH_key_production.generatePublicPrivatePair(gx,gy,a,p)

    receiverKeyX=sender_receiver_helper.receiveNumber(communicateSocket)
    receiverKeyY=sender_receiver_helper.receiveNumber(communicateSocket)
    #print("public key point is recieved from sender")
    #print(receiverKeyX,receiverKeyY)


    publicKeyX,publicKeyY=publicKey
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyX)
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyY)
    #print("public key point is sent to sender")
    #print(publicKey)
    
    sharedKey=ECDH_key_production.generateSharedKey(privateKey,(receiverKeyX,receiverKeyY),a,p)
    print("shared secret key:",hex(sharedKey))
    return sharedKey







while True:
    print("Waiting for a connection...")
    communicateSocket, client_address = server_socket.accept()
    print("Connected to", client_address)

    try:
        avg=0
        for i in range(5):
            print()
            print("run ",i+1)
            start=time.time()
            sharedKey=keyExchange(communicateSocket)
            end=time.time()
            avg+=end-start
            print("time for setting up shared secret key: ",(end-start)*1000,"ms")
        avg=avg/5
        print()
        print('average time: ',avg)
        print()






        bitstrings=bitStringOp.intToBitstrings(sharedKey)
        keyGeneration.ECDHKeygen(bitstrings)
        #print("done")




        received_bitstrings=sender_receiver_helper.receiveBitstrings(communicateSocket)


        start=time.time()
        message=AES_CBC.CBC_decrypt(received_bitstrings)
        #message=AES_CTR.CTR_decrypt(received_bitstrings)
        end=time.time()
        print("time for decryption: ",(end-start)*1000,"ms")

        print("recovered message:",message)
        #communicateSocket.sendall(data)
    finally:
        # Clean up the connection
        communicateSocket.close()
