import sys
import csv
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    name,type = sys.argv[1].split(".")
    if type != "csv":
        sys.exit("Not a CSV file")
    try:
        list = []
        names = []
        last=[]
        first=[]
        houses=[]
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file , fieldnames = ["name", "house"])
            for row in reader:
                names.append(row['name'])
                houses.append(row['house'])
            first.append("first")
            last.append("last")
            for name in  names[1:]:
                last_name, first_name = name.strip().split(",")
                last.append(last_name.strip())
                first.append(first_name.strip())

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            for i in range(len(first)):
                writer.writerow({"first": first[i] , "last": last[i], "house": houses[i]})

    except FileNotFoundError:
        sys.exit("Could not read ", sys.argv[1])

if __name__ == "__main__":
    main()
