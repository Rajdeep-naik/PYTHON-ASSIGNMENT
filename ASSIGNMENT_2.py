"""Assignment 2: Find the largest of three numbers using conditional statements."""


def find_largest(num1: float, num2: float, num3: float) -> float:
    """Evaluates and returns the largest among three numbers."""
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def main():
    print("=" * 45)
    print("       FIND LARGEST OF THREE NUMBERS")
    print("=" * 45)

    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        n3 = float(input("Enter third number: "))

        largest = find_largest(n1, n2, n3)
        print(f"\nThe largest number among {n1}, {n2}, and {n3} is: {largest}\n")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    main()