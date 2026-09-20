"""Assignment 3: Check whether a triangle is a right-angled triangle using functions."""


def is_right_angled_triangle(side1: float, side2: float, side3: float) -> bool:
    """Checks the Pythagorean theorem: a^2 + b^2 == c^2.

    Returns True if right-angled, False otherwise.
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False

    # Sort sides so the largest side is always the hypotenuse
    sides = sorted([side1, side2, side3])
    base, perpendicular, hypotenuse = sides[0], sides[1], sides[2]

    # Compare sum of squares using round to avoid float precision issues
    return round(base**2 + perpendicular**2, 5) == round(hypotenuse**2, 5)


def main():
    print(f'{"=" * 50}')
    print(f"{"RIGHT-ANGLED TRIANGLE CHECKER":^50}")
    print(f'{"=" * 50}')

    try:
        a = float(input("Enter length of side 1: "))
        b = float(input("Enter length of side 2: "))
        c = float(input("Enter length of side 3: "))

        if is_right_angled_triangle(a, b, c):
            print(
                f"\nResult: Sides ({a}, {b}, {c}) form a Right-Angled Triangle.\n"
            )
        else:
            print(
                f"\nResult: Sides ({a}, {b}, {c}) DO NOT form a Right-Angled Triangle.\n"
            )

    except ValueError:
        print("Invalid input. Please enter numerical values for side lengths.")


if __name__ == "__main__":
    main()