from twttr import shorten
import sys

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("1") == "1"
    assert shorten("NAME") == "NM"
    assert shorten("aeioU,") == ","

def main():
    test_shorten()


if __name__ ==  "__main__":
    main()
