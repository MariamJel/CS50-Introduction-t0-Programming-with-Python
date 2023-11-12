def main():
    prompt = input("input: ")
    print(f"Output: {shorten(prompt)}")

def shorten(word):
    new_word=""
    for k in range(len(word)):
        match word[k].lower():
            case  "a" | "e" | "i" | "o" | "u" :
                pass
            case _:
                new_word += word[k]
    return new_word

if __name__ == "__main__":
    main()




