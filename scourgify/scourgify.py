import sys
import csv

def main():
    # 1. Validate command-line arguments
    check_arguments()

    students = []

    # 2. Read from the input file (sys.argv[1])
    try:
        with open(sys.argv[1], "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                # Split "Last, First" into two parts
                last, first = row["name"].split(", ")
                
                # Append a new dictionary with the split names and the house
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # 3. Write to the output file (sys.argv[2])
    with open(sys.argv[2], "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        # Write the header row
        writer.writeheader()
        # Write all student data
        writer.writerows(students)

def check_arguments():
    # Expecting exactly 2 arguments + script name = length of 3
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Note: The prompt doesn't specify checking for .csv extension here,
    # but it requires checking if the file can be read.

if __name__ == "__main__":
    main()