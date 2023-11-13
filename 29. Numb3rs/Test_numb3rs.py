from numb3rs import validate
def main():
    test_validate_true()
    test_validate_false()

def test_IP_format():
    assert validate(r"255.255.255.255") == True
    assert validate(r"100.100.100.100") == True
    assert validate(r"100.100.100") == False
    assert validate(r"100.100") == False
    assert validate(r"100") == False
   

def test_IP_range():
    assert validate(r"256.0.0.0") == False
    assert validate(r"0.256.0.0") == False
    assert validate(r"0.0.256.0") == False
    assert validate(r"0.0.0.256") == False
    assert validate(r"255.255.255.255") == True

if __name__ == "__main__":
    main()
