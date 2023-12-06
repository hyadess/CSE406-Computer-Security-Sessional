import importlib

byteworks=importlib.import_module("1905064_byteworks")
keyGeneration=importlib.import_module("1905064_keyGeneration")
bitvector_demo=importlib.import_module("1905064_bitvector_demo")
import numpy as np

from BitVector import *
def bytesubstitution(array):
    
    for i in range(0,4):
        for j in range(0,4):
            array[i][j]=byteworks.byteSubstitute(array[i][j])
    return array

def shiftRow(array):
    
    for i in range(0,4):
        array[i]=np.roll(array[i],-i)
    return array


def addRoundKey(array,round):
    for j in range(0,4):
        for i in range(0,4):
            array[i][j]=format(int(array[i][j],2)^int(keyGeneration.keys[round][i][j],2),'08b')
    return array

def galoisFieldMul(array,row,column):
    ans=0
    for i in range (0,4):
        m1=BitVector(bitstring=array[i][column])
        m2=m1.gf_multiply_modular(bitvector_demo.Mixer[row][i],bitvector_demo.AES_modulus,8)
        curr=m2.intValue()
        ans=ans^curr
    ans=format(ans,'08b')
    return ans


def mixColumn(array):
    newArray=np.copy(array)
    for i in range(0,4):
        for j in range(0,4):
            newArray[i][j]=galoisFieldMul(array,i,j)
    return newArray


def msgArrayToString(array):
    str=""
    for i in range(0,4):
        for j in range(0,4):
            str=str+chr(int(array[j][i],2))
            #print(str)
    # str = ''.join([chr(int(''.join(row), 2)) for row in array])
    return str


def encryption(msg): # an  1d array of bitsrings is given, returns another 1d array of bitstrings

    np_msgArray=np.array(msg)
    row=column=4
    np_2dmsgArray=np.reshape(np_msgArray,(row,column))
    msgArray=np.transpose(np_2dmsgArray)  # 2d array of bitstrings is created

    msgArray=addRoundKey(msgArray,0) #round 0
   

    for i in range(1,10): # round 1 to 9
        msgArray=bytesubstitution(msgArray)
        msgArray=shiftRow(msgArray)
        msgArray=mixColumn(msgArray)
        msgArray=addRoundKey(msgArray,i)

    msgArray=bytesubstitution(msgArray)
    msgArray=shiftRow(msgArray)
    msgArray=addRoundKey(msgArray,10)


    #keyGeneration.showMatrix(msgArray)
    #str=msgArrayToString(msgArray)

    msgArray=np.transpose(msgArray)
    ans=msgArray.flatten()  # we converted into 1d array of bitstrings again

    return ans






# ciphertext=encryption('Two One Nine Two')

# #print("'"+ciphertext+"'")
