import sys
import os

def main():
    
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check for the correct file extension
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Try to open the file and count the lines
    try:
        count = count_lines(filename)
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(filename):
    lines_count = 0
    with open(filename, "r") as file:
        for line in file:
            
            stripped_line = line.lstrip()

            # Ignore blank lines
            if not stripped_line:
                continue
            
            # Ignore comments (lines starting with #)
            if stripped_line.startswith("#"):
                continue

            # If it's not a blank line or a comment, count it
            lines_count += 1
            
    return lines_count

if __name__ == "__main__":
    main()
