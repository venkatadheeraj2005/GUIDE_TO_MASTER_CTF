from Crypto.Util.number import long_to_bytes
a = input("Enter the Long number: ")
a = long_to_bytes(a.encode('utf-8'))
print(a)
