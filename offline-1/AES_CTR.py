
import secrets
import bitStringOp
import encryptOp
import decryptOp
import numpy as np

def CTR_encrypt(message):
    msgStrings=bitStringOp.msgDivide(message)

    #counter
    i=0
    #nonce generation
    nonce=secrets.randbits(128)  
    nonceBitStrings=bitStringOp.intToBitstrings(nonce)

    ciphertext=[]
    ciphertext.extend(nonceBitStrings)  #nonce is passed 
    for chunk in msgStrings:
        
        counterBitstrings=bitStringOp.intToBitstrings(i)
        inputXorBitStrings=bitStringOp.xoringBitstrings(nonceBitStrings,counterBitstrings) #xoring nonce ans counter
        encryptedBitStrings=encryptOp.encryption(inputXorBitStrings)  

        msgBitStrings=bitStringOp.msgToBitStrings(chunk)
        outputBitStrings=bitStringOp.xoringBitstrings(msgBitStrings,encryptedBitStrings)

        ciphertext.extend(outputBitStrings)
        i=i+1
    return ciphertext


def CTR_decrypt(array):  # input is an array of  bitstrings....
    siz=16
    #counter
    j=0
    #nonce retrieval
    nonceBitStrings=array[0:16]

    plaintext=[]
  
    for i in range(0, len(array), siz):  
        if i==0:
            continue
        curArray=array[i:i+siz]   # divided the array into arrays of 16 8bit bitstring...

        counterBitstrings=bitStringOp.intToBitstrings(j)
        inputXorBitStrings=bitStringOp.xoringBitstrings(nonceBitStrings,counterBitstrings) #xoring nonce ans counter
        encryptedBitStrings=encryptOp.encryption(inputXorBitStrings)  #not decryption ....

        xorBitstrings=bitStringOp.xoringBitstrings(curArray,encryptedBitStrings)
        plaintext.extend(xorBitstrings)
        j=j+1
        
        

    message = ''.join([chr(int(bitstring, 2)) for bitstring in plaintext]) # here, I am converting it into message string
    return message


print(CTR_decrypt(CTR_encrypt('I am proud. but no that much...... CTR is also done!!!!')))

