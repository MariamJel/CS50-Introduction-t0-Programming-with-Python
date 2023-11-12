from tabulate import tabulate
import sys
import csv
def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguements")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    name,type = sys.argv[1].split(".")
    if type != "csv":
        sys.exit("Not a CSV file")
    try:
        list = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[1])
                list.append(row)
            print(tabulate(list[1:], headers = list[0],  tablefmt = "grid"))



    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
