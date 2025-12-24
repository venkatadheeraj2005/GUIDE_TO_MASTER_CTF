import os
import sys

# --- Configuration ---
INPUT_FILE_LINES = 'input_lines.txt'
OUTPUT_FILE_SPACED = 'output_spaced.txt'

INPUT_FILE_SPACED = 'input_spaced.txt'
OUTPUT_FILE_LINES = 'output_lines.txt'
# ---------------------

def lines_to_spaced_string(input_filename, output_filename):
    """
    Reads numbers from a file (one per line) and writes them as a single, 
    space-separated string to an output file.
    """
    if not os.path.exists(input_filename):
        print(f"Error: Input file '{input_filename}' not found.", file=sys.stderr)
        return

    print(f"Reading from: {input_filename}")
    
    try:
        with open(input_filename, 'r') as f:
            # Read all lines, strip whitespace (including newline), and filter out empty lines
            numbers = [line.strip() for line in f if line.strip()]

        # Join the list elements into a single string separated by a space
        spaced_string = " ".join(numbers)

        with open(output_filename, 'w') as f:
            f.write(spaced_string)
            
        print(f"Success! Output written to: {output_filename}")
        print(f"Preview: '{spaced_string[:50]}...'")

    except Exception as e:
        print(f"An error occurred during conversion: {e}", file=sys.stderr)


def spaced_string_to_lines(input_filename, output_filename):
    """
    Reads a single, space-separated string of numbers from a file and 
    writes each number to a new line in an output file.
    """
    if not os.path.exists(input_filename):
        print(f"Error: Input file '{input_filename}' not found.", file=sys.stderr)
        return

    print(f"\nReading from: {input_filename}")
    
    try:
        with open(input_filename, 'r') as f:
            content = f.read().strip()
        
        # Split the content by spaces to get individual numbers
        numbers = content.split()
        
        # Join the list elements into a single string separated by a newline
        lines_string = "\n".join(numbers)

        with open(output_filename, 'w') as f:
            f.write(lines_string + "\n") # Add final newline for clean file formatting
            
        print(f"Success! Output written to: {output_filename}")
        print(f"Preview (first 5 numbers): {', '.join(numbers[:5])}...")

    except Exception as e:
        print(f"An error occurred during reverse conversion: {e}", file=sys.stderr)


if __name__ == "__main__":
    # --- Execution ---
    
    # Task 1: Convert multiline data to a single space-separated string
    lines_to_spaced_string(INPUT_FILE_LINES, OUTPUT_FILE_SPACED)

    # Task 2: Convert the space-separated string back to multiline data
    # (Assuming the output of Task 1 is used as input for Task 2)
    spaced_string_to_lines(OUTPUT_FILE_SPACED, OUTPUT_FILE_LINES)
    
    print("\nCheck your directory for the output files.")
