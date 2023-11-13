from um import count

def test_starts_with_um():
    assert count("Umbrella") == 0
def test_ends_with_um():
    assert count("Album") == 0
def test_upper_lower_case():
    assert count("Um, you are so, um, beautiful") == 2

if __name__ == "__main__":
    test_starts_with_um()
    test_ends_with_um()
    test_upper_lower_case()


