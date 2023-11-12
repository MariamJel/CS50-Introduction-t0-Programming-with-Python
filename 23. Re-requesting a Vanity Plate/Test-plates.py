from plates import is_valid

def test_length():
    assert is_valid("ABSDAS12") == False
    assert is_valid("A") == False
    assert is_valid("AS12") == True

def test_num_letters():
    assert is_valid("A123") == False

def number_placement():
    assert is_valid("A3AB") == False
    assert is_valid("12AFVS") == False
    assert is_valid("ABC1D3") == False
    assert is_valid("12346") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("AB12EF") == True
    assert is_valid("CSS222") == True
    assert is_valid("CS2222") == True
    assert is_valid("CS2A2S") == False
    assert is_valid("CSS22S") == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CSTG 3") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
    assert is_valid("AA 2 3") == False
    assert is_valid("CSTG 3") == False
    assert is_valid("CS!50") == False
    assert is_valid("AB") == True
    assert is_valid("ABC") == True
    assert is_valid("ABCD") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("QWERTYUI") == False


def test_punctuation():
    assert is_valid("AB,<3") == False

def test_zero_placement():
    assert is_valid("ABC012") == False
    assert is_valid("ABC120") == True




# def main():
#     test_length()
#     test_num_letters()
#     number_placement()
#     test_punctuation()
#     test_zero_placement()

# if __name__ == "__main__":
#     main()

# def main():
#     test_min_max()
#     test_two_letters()
#     test_middle_num()
#     test_zero()
#     test_symbols()

# def test_min_max():
#     assert is_valid("AB") == True
#     assert is_valid("ABC") == True
#     assert is_valid("ABCD") == True
#     assert is_valid("ABCDEF") == True
#     assert is_valid("A") == False
#     assert is_valid("QWERTYUI") == False

# def test_two_letters():
#     assert is_valid("AA") == True
#     assert is_valid("A2") == False
#     assert is_valid("2A") == False
#     assert is_valid("22") == False

# def test_middle_num():
#     assert is_valid("CSS222") == True
#     assert is_valid("CS2222") == True
#     assert is_valid("CS2A2S") == False
#     assert is_valid("CSS22S") == False
# def test_zero():
#     assert is_valid("CS50") == True
#     assert is_valid("CS05") == False
# def test_symbols():
#     assert is_valid("CS.50") == False
#     assert is_valid("CS 50") == False
#     assert is_valid("AA 2 3") == False
#     assert is_valid("CSTG 3") == False
#     assert is_valid("CS!50") == False


# if __name__ == "__main__":
#     main()
