import requests
import sys
import json
def main():
    bitcoin = bitcoins()
    amount = price(bitcoin)
    
    print(f"${amount:,.4f}")

def bitcoins():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line arguement")
    try:
        num = float(sys.argv[1])
        return num
    except ValueError:
        sys.exit("Invalid command-line arguement")

def price(number):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = float(response["bpi"]["USD"]["rate_float"])
    return rate*number


main()
