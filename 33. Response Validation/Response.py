from validator_collection import validators

def main():
    email_adress= input("What's your email adress? ")
    try :
        isValid = validators.email(email_adress)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
