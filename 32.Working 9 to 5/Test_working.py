
from working import convert
import pytest

def main():
    test_wrong_formar()
    test_time()
    test_wrong_hour()
    test_wrong_minutes()

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9am - 4pm")
def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("17 AM to 10 PM")
def test_wrong_minutes():
    with pytest.raises(ValueError):
        convert("9:70 AM to 2:60 PM")
def test_time():
    assert convert("9 AM to 4 PM") == "09:00 to 16:00"
    assert convert("11 PM to 7 AM") == "23:00 to 07:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("11:00 AM to 4:00 PM") == "11:00 to 16:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

if __name__ == "__main__":
    main()

