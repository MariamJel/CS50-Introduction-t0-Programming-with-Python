answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
def is_true(a):
    x = a.replace("-", " ").lower().strip()
   
    if x == "42" or x == "forty two":
        return True
if is_true(answer):
    print("Yes")
else:
    print("No")
