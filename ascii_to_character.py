print("------ ASCII to CHRACTER --------\n[1]File\n[2]Text")
choice = int(input("Enter Your Choice: "))

if choice == 2:
    input_str = input('Enter the list of ASCII numbers (space-separated): ')
    ords = [chr(int(o)) for o in input_str.split()]

    # Join the resulting characters into a single string
    result_string = "".join(ords)

    print(f"\nDecoded String: {result_string}")
if choice == 1:
	file_name = input("Enter the File Name with extention: ")
	ords = []
	try:
		with open(file_name, 'r') as f:
			for line in f:
				a = line.strip()
				if a.isdigit():
					ords.append(int(a))
		print("".join(chr(o) for o in ords))
	except FileNotFoundError:
    		print(f"Error: The file '{file_name}' was not found.")
	except Exception as e:
    		print(f"An error occurred: {e}")
