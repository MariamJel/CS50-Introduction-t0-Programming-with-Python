def make_list():
    grocery_list = {}
    while True:
        try:
            item = input("").upper()
            if item in grocery_list:

                    grocery_list[item] += 1

            else:
                    grocery_list.update({item : 1})

        except EOFError:
            for item in sorted(list(grocery_list.keys())):
                print(grocery_list[item], item)
            break

        except RuntimeError:
            pass
def main():
    make_list()

main()

