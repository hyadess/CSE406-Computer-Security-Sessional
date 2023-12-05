
import secrets
import bitStringOp
import encryptOp
import decryptOp
import numpy as np

def CBC_encrypt(message):
    msgStrings=bitStringOp.msgDivide(message)
    i=1
    cur=[]  #saves previous ciphertext..........
    ciphertext=[]
    for chunk in msgStrings:
        if i==1:
            IV=secrets.randbits(128)  #IV generation
            IVBitstrings=bitStringOp.intToBitstrings(IV)
            chunkBitstrings=bitStringOp.msgToBitStrings(chunk)
            xorBitStrings=bitStringOp.xoringBitstrings(IVBitstrings,chunkBitstrings) #xoring IV ans M0
            xorBitStrings=encryptOp.encryption(xorBitStrings)
            ciphertext.extend(IVBitstrings)  #adding IV at first
            ciphertext.extend(xorBitStrings)
            cur=xorBitStrings
        else:
            chunkBitstrings=bitStringOp.msgToBitStrings(chunk)
            xorBitStrings=bitStringOp.xoringBitstrings(cur,chunkBitstrings) #xoring previous C and M_i
            xorBitStrings=encryptOp.encryption(xorBitStrings)
            ciphertext.extend(xorBitStrings)
            cur=xorBitStrings
        i=i+1
    return ciphertext


def CBC_decrypt(array):  # input is an array of  bitstrings....
    siz=16
    prev=[]
    plaintext=[]
    for i in range(0, len(array), siz):  
        curArray=array[i:i+siz]   # divided the array into arrays of 16 8bit bitstring...
        if i>=1:  # no need to decrypt the IV!!!
            decrypted=decryptOp.decryption(curArray)
            xorBitstrings=bitStringOp.xoringBitstrings(decrypted,prev)
            plaintext.extend(xorBitstrings)
        prev=curArray

    message = ''.join([chr(int(bitstring, 2)) for bitstring in plaintext]) # here, I am converting it into message string
    return message


print(CBC_decrypt(CBC_encrypt('I am proud. but no that much...... now I can add more and more!!!!??????______!')))




















# Example
message_chunk = "abc"
xor_number = 0x0


# Example
# message = "This is a sample message. but lets see what can happen to be here"
# result = divide_into_128_bit_strings(message)

# print(result)