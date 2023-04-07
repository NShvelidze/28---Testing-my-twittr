vowels = ["A", "E", "I", "O", "U"]

def main():
    word = input("Input: ")
    word_without_vowels = shorten(word)
    print("Output:", word_without_vowels)

def shorten(word):
    for x in word:
        if x.upper() in vowels:
            word = word.replace(x,"")
    return word

if __name__ == "__main__":
    main()
