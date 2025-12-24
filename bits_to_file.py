def bits_to_file(bit_file_path, output_file_path):
    try:
        with open(bit_file_path, 'r') as f:
            binary_string = f.read().strip()

        # Pad with zeros to make the length a multiple of 8
        padding = 8 - len(binary_string) % 8
        if padding != 8:
            binary_string += '0' * padding

        # Convert bit string to bytes
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte = int(binary_string[i:i+8], 2)
            byte_array.append(byte)
        
        # Write bytes to a new file
        with open(output_file_path, 'wb') as f_out:
            f_out.write(byte_array)
        print(f"Binary data written to {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Usage ---
# bits_to_file('LSB_Report.txt', 'hidden_data.bin')
if __name__ == "__main__":
	bit_file = input('Enter the bits file path: ')
	bits_to_file(bit_file , 'hidden_data.bin') 
