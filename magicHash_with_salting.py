import hashlib
import itertools
import string

SALT = "c789abc318a2d1ac"
#TARGET_HASH = "0e901030918301310378749512009101"

# Function to check the required format
def is_magic_hash(h):
    # Check if hash starts with '0e'
    if h[0] == '0' and h[1] == 'e':
        # Check if the rest of the string is ALL digits
        return h[2:].isdigit()
    return False

common_wordlist = "/usr/share/john/password.lst"
# Brute-force loop (using a wordlist or random strings)
print(1)
count =1
for password in common_wordlist:
    input_string = SALT + password
    print(input_string)
    if count ==2:
        print("test1")
    count +=1
    generated_hash = hashlib.md5(input_string.encode()).hexdigest()
#    print(generated_hash)
    # If the generated hash is a "magic hash", we found our exploit!
    if is_magic_hash(generated_hash):
        print(f"Found Exploit Password: {password}")
        break
