from seasons import check_birthday

def test_check_birthday():
    assert check_birthday("1998-07-20") ==("1998", "07", "20")
    assert check_birthday("1998-7-20") == None
    assert check_birthday("July 20, 1998") == None

def main():
    test_check_birthday()

if __name__ == "__main__":
    main()
