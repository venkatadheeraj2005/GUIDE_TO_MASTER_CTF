import numpy as np
from PIL import Image

image_path = input('enter the file path')
image  = Image.open(image_path, "r")
pixels = np.array(image.getdata())

num_channels   = 0
ls_bits        = ""
hidden_message = ""

if   image.mode == "RGB":  num_channels = 3
elif image.mode == "RGBA": num_channels = 4
else:
    print("Cannot process this image because it's not supported.")
    exit(0)

# num_pixels = len(pixels)
num_pixels = pixels.size // num_channels

# create a concatenation of all the LSBs (for each channel of each pixel)
for i in range(num_pixels):
    for j in range(num_channels):
        ls_bits += bin(pixels[i][j])[-1]

# from the previous concatenation, create a list of 8-bits chunks
ls_bits = [ls_bits[i:i+8] for i in range(0, len(ls_bits), 8)]

# from the previous list, create a concatenation of all the ASCII characters
# corresponding to the chunks
for i in range(len(ls_bits)):
    hidden_message += chr(int(ls_bits[i], 2))

print(hidden_message)
