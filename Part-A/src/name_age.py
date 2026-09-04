"""Calculates a user's approximate birth year based on their age.

Input:
    user_name: The user's name as a string from keyboard input.
    user_age: The user's age as an integer from keyboard input.

Process:
    Subtract the user's age from the current year to find their birth year.

Output:
    A personalized greeting with the calculated birth year to the console.

Typical usage example:
    Enter your name: Darrius Brooks
    Enter your age: 26
    Hello Darrius Brooks! You were born in or around 2000.
"""

# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    print(f"Hello {user_name}! You were born in or around {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()
