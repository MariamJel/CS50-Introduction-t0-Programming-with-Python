from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    bday = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(bday)
    except:
        sys.exit("Invalid Date")
    date_of_birth = date(int(year), int(month), int(day))
    today = date.today()
    duration = today - date_of_birth
    total_minutes = duration.days * 24 * 60
    words = p.number_to_words(total_minutes, andword = "")
    print(words.capitalize(), "minutes")

def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
