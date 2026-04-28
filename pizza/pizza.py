import sys
import csv
from tabulate import tabulate

def main():
    # 1. Check command-line arguments
    check_arguments()

    try:
        # 2. Open and read the CSV file
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            table = []
            for row in reader:
                table.append(row)
            
            # 3. Print the table using tabulate with "grid" format
            # headers="firstrow" tells tabulate to use the first list in 'table' as the header
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_arguments():
    # Check if user provided too few arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    # Check if user provided too many arguments
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    # Check if the file extension is .csv
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()    

        