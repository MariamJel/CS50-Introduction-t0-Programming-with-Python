import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    isCorrect = re.search(r"^((1[0-2]|[0-9])(:([0-5][0-9]))*) ([A-P]M) to ((1[0-2]|[0-9])(:([0-5][0-9]))*) ([A-P]M)$", s)
    if isCorrect:
        group = isCorrect.groups()
        startingHour = group[1]
        startingMinutes = group[3]
        startingAP = group[4]
        endingHour = group[6]
        endingMinutes = group[8]
        endingAP = group[9]
        convertStart=new_format(startingHour,startingMinutes,startingAP)
        convertEnd=new_format(endingHour, endingMinutes, endingAP)
        return(f"{convertStart} to {convertEnd}")
    else:
        raise ValueError

def new_format(hour, minutes, AP):
    if AP == "AM":
        if int(hour) == 12:
            hour = "00"
        elif int(hour)<10:
            hour = "0" + hour
    elif AP == "PM":
        if int(hour) == 12:
            hour == 12
        else:
            hour = int(hour) + 12

    if minutes and minutes != "00":
        if int(minutes)<10:
            minutes = "0" + minutes
        return f"{hour}:{minutes}"
    else:
        return f"{hour}:00"



if __name__ == "__main__":
    main()
