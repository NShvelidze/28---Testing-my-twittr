from twttr import shorten

def main():
    test_cases()

def test_cases():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("TWiTter") == "TWTtr"

if __name__ == "__main__":
    main()
