def main():
    fraction = input("Gauge? ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    if not x.is_integer() or not y.is_integer() or x > y:
        raise ValueError("Condition not met: x and y should both be integers, and x should not be greater than y.")

    return round(x/y*100)



def gauge(percentage):

        if percentage <= 1:
            result = "E"
            return result
        elif percentage >= 99:
            result = " F "
            return result
        else:
            result = str(percentage) + '%'
            return result



if __name__ == "__main__":
    main()
