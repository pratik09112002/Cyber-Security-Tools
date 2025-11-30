import re

def check_password_strength(password: str) -> str:
    length_score = len(password) >= 12
    upper_score = bool(re.search(r"[A-Z]", password))
    lower_score = bool(re.search(r"[a-z]", password))
    digit_score = bool(re.search(r"\d", password))
    special_score = bool(re.search(r"[^\w\s]", password))

    score = sum([length_score, upper_score, lower_score, digit_score, special_score])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


def give_suggestions(password: str) -> list:
    suggestions = []

    if len(password) < 12:
        suggestions.append("Use at least 12 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters (A-Z).")
    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters (a-z).")
    if not re.search(r"\d", password):
        suggestions.append("Add digits (0-9).")
    if not re.search(r"[^\w\s]", password):
        suggestions.append("Add special characters (e.g. !, @, #, ?).")

    if not suggestions:
        suggestions.append("Good job! Your password looks strong.")

    return suggestions


def main():
    print("=== Password Strength Analyzer ===")
    password = input("Enter a password to analyze: ")

    strength = check_password_strength(password)
    print(f"\nStrength: {strength}")

    print("\nSuggestions:")
    for s in give_suggestions(password):
        print(f"- {s}")


if __name__ == "__main__":
    main()
