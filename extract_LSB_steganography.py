import os
from PIL import Image

def lsbsFromImage(image_path):
	try:
		img = Image.open(image_path)
	except Exception as e:
		print('Error: ', e)
		return ""

	img = img.convert('RGB')

	LSB_bits = []
	for pixel in img.getdata():
		for color in pixel:
			lsb = color & 1
			LSB_bits.append(str(lsb))
	return ''.join(LSB_bits)

if __name__ == "__main__" :
	image_file = input("Enter the File Path: ")
	if not os.path.exists(image_file):
		print("Error: File not found!")
		exit(1)
	hidden_message = lsbsFromImage(image_file)

	if hidden_message:
		base_dir = os.path.dirname(image_file)
		output_path = os.path.join(base_dir, 'LSB_Report.txt')
		with open(output_path, 'w') as f:
			f.write(hidden_message)
	print(f"Successfully extracted LSBs to {output_path}")










