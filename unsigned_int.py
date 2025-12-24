#data_str = "-65 -56 58 95 -77 82 22 -49 -88 -61 -87 -17 33 72 -125 -107 -86 59 13 -34 -26 -38 -43 37 -73 31 111 -47 -124 117 -83 68 61 -24 -93 -16 58 -71 -65 -30 124 104 -47 -99 -80 85 51 90 -112 64 57 118 26 14 -101 -46 45 10 -93 -78 127 81 -10 -68 57 -103 -83 115 82 108 85 -49 -43 39 108 -123 124 -97 -32 12 -32 25 -126 -6 39 29 -52 85 40 112 7 -89 -63 -3 100 -6 -106 17 109 -24 125 -62 -73 82 -23 36 -40 101 -61 -72 113 -93 -47 -13 -98 -8 17 106 77 57 -38 84 -32 -101 81 68 -107 -25 85 2 -48 -45 -59 -121 37 -82 -85 -3 20 111 -75 -123 18 -122 121 -80 127 -118 27 -52 -61 -11 33 -93 -111 114 -24 38 90 61 41 42 16 -18 -79 54 -100 93 51 -80 -52 -23 54 -34 111 -81 -113 -18 57 -86 -69 -4 -97 -36 -97 48"

with open('ctf.txt', 'r') as f:
    data_str = f.read()
# 1. Parse the string into a list of integers
#print(data_str)
signed_ints = [int(n) for n in data_str.split()]
#print(signed_ints)
# 2. Convert to unsigned 8-bit integers (bytes)
# Python handles 8-bit signed to unsigned conversion implicitly using the mask & 0xFF 
# or by simply using the 'bytes' constructor if the numbers are pre-validated as int8
# We will use a list comprehension for clarity:
unsigned_bytes_list = [n & 0xFF for n in signed_ints]
byte_stream = bytes(unsigned_bytes_list)
print(unsigned_bytes_list)
# 3. Attempt to decode the byte stream using ASCII
try:
    decoded_text = byte_stream.decode('ascii')
    print("Decoded Text:\n" + "="*50)
    print(decoded_text)
    print("="*50)
except UnicodeDecodeError:
    print("Could not decode directly to ASCII. Outputting raw byte data for further analysis.")
