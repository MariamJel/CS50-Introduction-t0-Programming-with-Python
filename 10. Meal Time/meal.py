def main():
    mealTime = input("What time is it? ")
    convertedTime = convert(mealTime)

    if  convertedTime >= 7 and convertedTime <=8 :
        print("breakfast time")
    if convertedTime >= 12 and convertedTime <=13:
        print("lunch time")
    if convertedTime >= 18 and convertedTime <=19:
        print("dinner time")

def convert(n):

    hour, minute = n.split(":")

    return  float(hour) + float(minute) / 60


if __name__ == "__main__":
    main()
