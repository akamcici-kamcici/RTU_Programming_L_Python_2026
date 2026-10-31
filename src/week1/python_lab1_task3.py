"""
Task 3 – Function with Combined Logic
-------------------------------------
Write a function `analyze_sentence(text)` that returns a tuple of three values.
"""
# Ahmet KAMCICI 241AEC014

def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (length, word count, contains 'python') for the given text."""
    length = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()

    return (length, word_count, contains_python)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    length, words, contains_python = analyze_sentence(sentence)

    print(f"Characters: {length}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {contains_python}")