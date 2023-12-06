import socket
import time
import pickle
import importlib
encryptOp=importlib.import_module("1905064_encryptOp")
AES_CBC=importlib.import_module("1905064_AES_CBC")
AES_CTR=importlib.import_module("1905064_AES_CTR")
sender_receiver_helper=importlib.import_module("1905064_sender_receiver_helper")
ECDH_key_production=importlib.import_module("1905064_ECDH_key_production")
keyGeneration=importlib.import_module("1905064_keyGeneration")


communicateSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
communicateSocket.connect(server_address)



#sender will send gx,gy,a,b,p, public key.................
#will receive receiver's public key..
#create shared secret key.................
def keyExchange(communicateSocket):
    p = 2**128 - 3
    a = 2
    b = 2
    gx = 5
    gy = 1
  
    sender_receiver_helper.sendNumber(communicateSocket,gx)
    sender_receiver_helper.sendNumber(communicateSocket,gy)
    print("point G is sent")
    sender_receiver_helper.sendNumber(communicateSocket,a)
    sender_receiver_helper.sendNumber(communicateSocket,b)
    print(" parameters a and b are sent")
    sender_receiver_helper.sendNumber(communicateSocket,p)
    print("prime p is sent")



    privateKey,publicKey=ECDH_key_production.generatePublicPrivatePair(gx,gy,a,p)
    publicKeyX,publicKeyY=publicKey
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyX)
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyY)
    print("public key point is sent to receiver")
    print(publicKey)


    receiverKeyX=sender_receiver_helper.receiveNumber(communicateSocket)
    receiverKeyY=sender_receiver_helper.receiveNumber(communicateSocket)
    print("public key point is recieved from receiver")
    print(receiverKeyX,receiverKeyY)


    sharedKey=ECDH_key_production.generateSharedKey(privateKey,(receiverKeyX,receiverKeyY),a,p)
    print(sharedKey)






try:
    #keyExchange(communicateSocket)
    keyGeneration.inputKeyGen()
    message = input("enter the message: ")

    start=time.time()
    #msgArray=AES_CBC.CBC_encrypt(message)
    msgArray=AES_CTR.CTR_encrypt(message)
    end=time.time()
    print("time for encryption: ",(end-start)*1000,"ms")

    sender_receiver_helper.sendBitstrings(communicateSocket,msgArray)

    # Receive the response from the server
    # data = communicateSocket.recv(1024)
    # print("Server response:", data.decode())
finally:
    # Clean up the connection
    communicateSocket.close()
