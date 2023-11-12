import random
def main():
    level = get_level()
    score = 0

    for n in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for tries in range(3):
            answer = int(input(f"{x} + {y} = "))
            right = x+y
            if answer == right:
                score += 1
                break
            elif tries == 2:
                print(f"{x} +{y} ={x+y}")

            else:
                print("EEE")
    print(score)

def get_level():
    while(True):
        try:
            n = int(input("Level: "))
            if(n > 0 and n <= 3):
                break
        except ValueError:
            pass
    return n

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
