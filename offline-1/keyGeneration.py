import numpy as np
import byteworks

def showMatrix(array):
    hex_array = np.vectorize(lambda x: hex(int(x, 2)))(array)
    print(hex_array)

def generate_round_constants():
    roundingConstants=np.array([[0x01,0x00,0x00,0x00]])
    for i in range(1, 10):  # AES-128 has 10 rounds
        prevConst = roundingConstants[i-1][0]
        #print(prevConst)
        newConst = (prevConst << 1) ^ (0x11b & -(prevConst >> 7))
        newRow=np.array([newConst,0x00,0x00,0x00])
        roundingConstants=np.vstack((roundingConstants,newRow))
    #print(roundingConstants)
    return roundingConstants

roundingConstants=generate_round_constants()
#print(roundingConstants)


def keyToBinary(str):
    keyArray = []
    for char in str:
        keyArray.append(format(ord(char), '08b'))

    np_1dArray=np.array(keyArray)
    row=column=4
    np_2dArray=np.reshape(np_1dArray,(row,column))
    #showMatrix(np_2dArray)
    return np_2dArray


def gFunction(array,round):
    newArray=np.copy(array)

    newArray[3]=np.roll(newArray[3],-1)
    for i in range(0,4):
        newArray[3][i]=byteworks.byteSubstitute(newArray[3][i])
        newArray[3][i]=format(roundingConstants[round][i]^int(newArray[3][i],2),'08b')
    
    #showMatrix(newArray)
    return newArray



def oneRoundKey(array,round):
    gValue=gFunction(array,round-1)
    nextArray=np.copy(array)
    for i in range(0,4):
        nextArray[0][i]=format(int(array[0][i],2)^int(gValue[3][i],2),'08b')
    for j in range(1,4):
        for i in range(0,4):
            nextArray[j][i]=format(int(array[j][i],2)^int(nextArray[j-1][i],2),'08b')
    
    return nextArray


def keyGeneration(str):
    keys=[]
    keys.append(keyToBinary(str)) #round 0 key...................
    for i in range(1,11):
        prevkey=keys[i-1]
        keys.append(oneRoundKey(prevkey,i))
    for i in range(0,11):
        keys[i]=np.transpose(keys[i])
    #showMatrix(keys)
    return keys


keys=keyGeneration('Thats my Kung Fu')
# showMatrix(keys)