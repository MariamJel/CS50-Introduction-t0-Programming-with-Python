import sys

def main():
    line_count = 0
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")

    name,lang = sys.argv[1].split(".")
    if lang != "py":
        sys.exit("Not a Python file")
    try:

        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if len(line) != 0:
                    if line[0] != "#":
                        line_count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_count)

if __name__ == "__main__":
    main()
