import unittest
from fuel import convert, gauge

def test_convert():
    assert convert("5/10") == 50
    assert convert("1/100") == 1
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

class Test_Convert_Errors(unittest.TestCase):
    def test_convert_raises_value_error_on_y_zero(self):
        with self.assertRaises(ZeroDivisionError):
            convert("4/0")  # Testing if convert raises ZeroDivisionError when y is 0

    def test_convert_raises_value_error_on_x_greater_than_y(self):
        with self.assertRaises(ValueError):
            convert("4/3")  # Testing if convert raises ValueError when x > y



if __name__ == "__main__":
    test_convert()
    test_gauge()
    unittest.main()
