from pwn import xor
FLAG = int(input("flag : "), 16)
FLAG = xor(FLAG, 1)
flag_bytes = FLAG.to_bytes((FLAG.bit_length() + 7)//8, "big")
print(flag_bytes)
