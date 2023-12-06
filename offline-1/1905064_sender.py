import socket
import time
import pickle
import importlib
from sympy import prevprime
from random import randint
import math
encryptOp=importlib.import_module("1905064_encryptOp")
AES_CBC=importlib.import_module("1905064_AES_CBC")
AES_CTR=importlib.import_module("1905064_AES_CTR")
sender_receiver_helper=importlib.import_module("1905064_sender_receiver_helper")
ECDH_key_production=importlib.import_module("1905064_ECDH_key_production")
keyGeneration=importlib.import_module("1905064_keyGeneration")
bitStringOp=importlib.import_module("1905064_bitStringOp")

communicateSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
communicateSocket.connect(server_address)

p = 2**128 - 159
a = 3
b = 4
gx = 5
gy = 12



def randomGeneration():

    # we will randomly generate p,a,gx,gy and then calculate b....................
    global p
    offset=randint(1,2**20)
    p=prevprime(2**128-offset) #to add some randomness.........................


    offset=randint(1,2**20)
    E=prevprime(p + 1 - int(math.sqrt(p))-offset)  # E is atleast p+1 - root (p)  ..and offset for randomness

    global a
    a=randint(2,E-1)%p
    global gx
    gx=randint(1,2**25)%p # as we need to cube it
    global gy
    gy=randint(1,2**25)%p
    global b
    b=((gy*gy)%p -(((gx*gx)%p)*gx)%p-(a*gx)%p)%p


#sender will send gx,gy,a,b,p, public key.................
#will receive receiver's public key..
#create shared secret key.................
def keyExchange(communicateSocket):
    randomGeneration()
  
    sender_receiver_helper.sendNumber(communicateSocket,gx)
    sender_receiver_helper.sendNumber(communicateSocket,gy)
    #print("point G is sent")
    sender_receiver_helper.sendNumber(communicateSocket,a)
    sender_receiver_helper.sendNumber(communicateSocket,b)
    #print(" parameters a and b are sent")
    sender_receiver_helper.sendNumber(communicateSocket,p)
    #print("prime p is sent")



    privateKey,publicKey=ECDH_key_production.generatePublicPrivatePair(gx,gy,a,p)
    publicKeyX,publicKeyY=publicKey
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyX)
    sender_receiver_helper.sendNumber(communicateSocket,publicKeyY)
    #print("public key point is sent to receiver")
    #print(publicKey)


    receiverKeyX=sender_receiver_helper.receiveNumber(communicateSocket)
    receiverKeyY=sender_receiver_helper.receiveNumber(communicateSocket)
    #print("public key point is recieved from receiver")
    #print(receiverKeyX,receiverKeyY)


    sharedKey=ECDH_key_production.generateSharedKey(privateKey,(receiverKeyX,receiverKeyY),a,p)
    print("shared secret key:",hex(sharedKey))
    return sharedKey






try:

    #way 1....................................
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


    ##way 2................................

    #keyGeneration.inputKeyGen()





    message = input("enter the message: ")

    start=time.time()
    msgArray=AES_CBC.CBC_encrypt(message)
    #msgArray=AES_CTR.CTR_encrypt(message)
    end=time.time()
    print("time for encryption: ",(end-start)*1000,"ms")

    sender_receiver_helper.sendBitstrings(communicateSocket,msgArray)

    # Receive the response from the server
    # data = communicateSocket.recv(1024)
    # print("Server response:", data.decode())
finally:
    # Clean up the connection
    communicateSocket.close()
