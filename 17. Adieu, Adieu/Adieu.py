import inflect
p = inflect.engine()


def get_names():
    name_list=[]


    while(True):
        try:
            name_list.append(input("Name: "))

        except EOFError:

            return name_list


def main():
    names = get_names()
    joined = p.join(names)
    print("\nAdieu, adieu, to", joined)

main()
