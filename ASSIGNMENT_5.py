"""Assignment 5: Check if a string contains only a-z, A-Z, and 0-9 using re.search()."""

import re


def check_allowed_characters(text):
    # Pattern validates that the string contains only alphanumeric characters from start (^) to end ($)
    pattern = r"^[a-zA-Z0-9]+$"

    # re.search scans the text and matches the whole string due to ^ and $ anchors
    if re.search(pattern, text):
        return True
    return False


def main():
    print(f'{"=" * 55}')
    print(f"{'ALPHANUMERIC STRING VALIDATOR':^55}")
    print(f'{"=" * 55}')

    user_input = input("Enter a string: ")

    if check_allowed_characters(user_input):
        print(
            "\nResult: The string contains ONLY valid characters (a-z, A-Z, 0-9)."
        )
    else:
        print(
            "\nResult: The string contains INVALID characters (spaces, symbols, etc.)."
        )


if __name__ == "__main__":
    main()