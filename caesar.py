def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result
def brute_force_caesar(text):
    for shift in range(26):
        print(f"Shift {shift}: {caesar_cipher(text, shift, mode='decrypt')}\n")
message = input('enter the message:')
n=int(input('1) Brute Force \n2) shift \nChoice :'))
if(n == 1):
	brute_force_caesar(message)
else:
	shift = int(input('\nenter the shift: '))
	print(caesar_cipher(message, shift))

