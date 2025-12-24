import os

def binaryToStr(file_path):
	try:
		with open(file_path, 'r') as f:
			binary_string = f.read().replace(' ', '').replace('\n', '')
		if len(binary_string) % 8 != 0:
			print("[ERROR] The number of bits is not a multiple of 8")
			return

		string = ""
		for i in range(0, len(binary_string), 8):
			byte = binary_string[i:i+8]
			char = chr(int(byte, 2))
			string += char
		print("The secrte Message : ", string)

	except FileNotFoundError:
		print('[ERROR] In opening File ')
	except ValueError:
           	print('[ERROR] The file contains invalid binary data.')
	except Exception as e:
        	print(f"[ERROR] An unexpected error occurred: {e}")

if __name__ == '__main__':
	file_path = input('Enter the location of the file :')
	binaryToStr(file_path)
