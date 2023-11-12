from random import randint
import sys

def get_n():
    number = input("Level: ")
    while(True):
        try:
            n = int(number)
            if(n > 0):
                break
            number = input("Level: ")
        except ValueError:
            pass
    return n

def guessed(n):
    while(True):
        while(True):
            try:
                guess = int(input("Guess: "))
                if(guess > 0):
                    break
            except ValueError:
                pass
        if(n < guess):
            print("Too large!")
        elif(n > guess):
            print("Too small!")
        else:
            break
    return True



def main():
    num = get_n()
    level = randint(1, num + 1)
    if guessed(level):
        sys.exit("Just right!")


main()





