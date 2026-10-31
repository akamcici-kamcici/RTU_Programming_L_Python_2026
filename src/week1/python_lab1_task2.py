"""
Task 2 – Greeting Function with String Manipulation
---------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces at the start and end with .strip()
- capitalizes the first letter with .capitalize()
- returns exactly: "Hello, <Name>! Welcome to Python!"
- if the name is empty (or only spaces), uses "Stranger" as the name
"""
# Ahmet KAMCICI 241AEC014

def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    clean_name = name.strip()

    if clean_name == "":
        clean_name = "Stranger"
    else:
        clean_name = clean_name.capitalize()

    return f"Hello, {clean_name}! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))