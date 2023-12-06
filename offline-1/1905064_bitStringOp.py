

#in this file, the functions convert integer or messages to array of bitstrings...
#also, we have array of bitstring xor operation.................


def intToBitstrings(integer_value): #large int to array of bitstrings............

    binary_string = bin(integer_value)

    binary_string = binary_string[2:].zfill(128)

    bitstring_array = [binary_string[i:i + 8] for i in range(0, 128, 8)]

    return bitstring_array


def msgToBitStrings(str):
    keyArray = []
    for char in str:
        keyArray.append(format(ord(char), '08b'))
    
    return keyArray


def msgDivide(message):  #devide the message into 128 bit strings.......
    
    msgBytes = message.encode('utf-8')

    chunkCount = (len(msgBytes) + 15) // 16

    stringList = [msgBytes[i*16:(i+1)*16] for i in range(chunkCount)]

    if len(stringList[-1]) < 16:
        space_padding = b' ' * (16 - len(stringList[-1]))
        stringList[-1] += space_padding

    stringList = [chunk.decode('utf-8') for chunk in stringList]

    return stringList


def xoringBitstrings(arr1, arr2):

    concatenated_str1 = ''.join(arr1)
    concatenated_str2 = ''.join(arr2)

    # XOR the entire sequences
    xor = int(concatenated_str1, 2) ^ int(concatenated_str2, 2)
    xorBitStrings=intToBitstrings(xor)

    return xorBitStrings




# print(msgToBitStrings('abc'))
# print(intToBitstrings(10))