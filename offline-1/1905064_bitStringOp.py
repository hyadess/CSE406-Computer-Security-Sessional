import fitz  # PyMuPDF library for PDF
from PIL import Image
import io
import os



#in this file, the functions convert integer or messages to array of bitstrings...
#also, we have array of bitstring xor operation.................


#also, we have functions to convert pdf and images to bitstrings......

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













# def pdfToBits(path):
#     bit_sequence = ""
#     pdf_document = fitz.open(path)

#     for page_number in range(pdf_document.page_count):
#         page = pdf_document[page_number]
#         pixmap = page.get_pixmap()
#         image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
#         image = image.convert('L') #grayscale
#         bit_sequence += ''.join(format(pixel, '08b') for pixel in image.tobytes())
#     pdf_document.close()
#     return bit_sequence



# def imageToBits(path):
#     with open(path, 'rb') as image_file:
#         image = Image.open(image_file).convert('L')
#     bit_sequence = ''.join(format(pixel, '08b') for pixel in image.tobytes())

#     return bit_sequence



# def create_2d_array(bit_sequence):
   
#     padded_bit_sequence = bit_sequence.ljust((len(bit_sequence) + 7) // 8 * 8, '0')

   
#     num_rows = len(padded_bit_sequence) // 16
#     array_2d = [[padded_bit_sequence[i:i+8] for i in range(j*row_length, (j+1)*row_length, 8)]
#                 for j in range(num_rows)]

#     return array_2d





# current_directory = os.getcwd()
# pdf_path = os.path.join(current_directory, 'objectFiles/sender/sample.pdf')
# bitSeq = pdfToBits(pdf_path)
# print("PDF Bit Sequence length:", len(bitSeq))
# print(bitSeq)

# path = 'example.jpg'
# image_bit_sequence = image_to_bit_sequence(path)
# print("Image Bit Sequence length:", len(image_bit_sequence))























# print(msgToBitStrings('abc'))
# print(intToBitstrings(10))