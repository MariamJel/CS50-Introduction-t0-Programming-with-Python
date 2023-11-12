months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("date: ")
        if "/" in date:
            month, day, year = date.split("/")
        else:
            if "," in date:
                month, day, year = date.replace(',',"").split()
                if month in months:
                        month = months.index(month) + 1

        if month in months or 1 <= int(month) <= 12:

            if int(year) >= 0 and 1 <= int(day) <= 31:

                print(f"{int(year):04}-{int(month):02}-{int(day):02}")
                break
    except ValueError:
        pass
    except NameError:
        pass










