from bank import value

def test_value():
    assert value("hello") == "$0"
    assert value("1") == "$100"
    assert value("Hello, Mariam") == "$0"
    assert value("How are you?") == "$20"

def main():
    test_value()


if __name__ ==  "__main__":
    main()
