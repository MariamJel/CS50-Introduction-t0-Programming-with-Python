def main():
    order()

def order():
    price = 0
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    while True:
        try:
            order_item = input("Item: ").title()
            for item in menu:
                if item == order_item:
                    price += menu[item]
                    print(f"Total: ${price:.2f}")
                    break

        except EOFError:
            print("\n")
            break
main()

