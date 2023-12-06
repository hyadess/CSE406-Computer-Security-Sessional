import struct
import socket
import pickle



#we will work with array of bitstrings....................
def sendBitstrings(socket, array):
    
    
    serialized = pickle.dumps(array)

    arrayLen = len(serialized).to_bytes(8, byteorder='big')
    socket.sendall(arrayLen)

    socket.sendall(serialized)



def receiveBitstrings(socket):
    # the size of the array of bitstrings..........
    arrLen = socket.recv(8)
    arrLen = int.from_bytes(arrLen, byteorder='big')

  
    serialized = socket.recv(arrLen) 
    #deserialize
    receivedBitstrings = pickle.loads(serialized)
    #print(receivedBitstrings)
    return receivedBitstrings

      




def sendNumber(socket,number):
    byted = number.to_bytes(16, byteorder='big')

    socket.sendall(byted)

def receiveNumber(socket):
    byted = socket.recv(16)  
    received = int.from_bytes(byted, byteorder='big')
    #print(hex(received))
    return received
