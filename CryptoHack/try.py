from Crypto.Util.number import long_to_bytes
from pwn import xor
import binascii

hex_string = input('Enter the hex string : ') 
key1 = binascii.unhexlify(hex_string)

hex_string = input('Enter the hex string : ') 
byte_data2 = binascii.unhexlify(hex_string)

key2 = xor(key1, byte_data2)

hex_string = input('Enter the hex string : ') 
byte_data3 = binascii.unhexlify(hex_string)

hex_string = input('Enter the hex string : ') 
byte_data4 = binascii.unhexlify(hex_string)

a = xor(byte_data4, byte_data3)
print("FLAG ^ KEY1 : ", a)
print('_____________________________________________________________________________________________________')
print('FLAG: ', xor(a ,key1).hex())


#message = xor(n, 13)   # Convert integer to bytes
#print(message)               # Raw bytes
#  print(message.decode())      # Decode to string (if printable)
