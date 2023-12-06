
import importlib
bitvector_demo=importlib.import_module("1905064_bitvector_demo")

def binaryConvert(char):
    ascii= ord(char)
    binary= format(ascii, '08b')
    #print(binary)
    return binary  #returns as a bitstring

def byteSubstitute(byte):  # a 8 bit bytestring should be given.................
    row=int(byte[0:4],2)
    column=int(byte[4:],2)
    #print(column)
    subByte=bitvector_demo.Sbox[16*row+column]
    subByte=format(subByte, '08b')
    
    #print(subByte)
    return subByte  #returns as a bitstring

def invByteSubstitute(byte):  # a 8 bit bytestring should be given.................
    row=int(byte[0:4],2)
    column=int(byte[4:],2)
    #print(column)
    subByte=bitvector_demo.InvSbox[16*row+column]
    subByte=format(subByte, '08b')
    
    #print(subByte)
    return subByte  #returns as a bitstring

#byteSubstitute(binaryConvert('B'))
#byteSubstitute('01100111')


