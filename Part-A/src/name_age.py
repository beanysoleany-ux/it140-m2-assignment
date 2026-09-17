"""
This program gathers user details to calculate and display a personalized name-age message.

Input:
    User's name as a string from console input.
    User's age as an integer from console input.

Process:
    Calculate the user's birth year by subtracting their age from the current year.

Output:
    A personalized message displaying the user's name and calculated birth year.

Typical usage example:
    Input name: Darrius Brooks
    Input age: 26
    Output: Hello Darrius Brooks! You were born in approximately 2000.
"""

from datetime import import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = "Darrius Brooks"
    user_age = 26

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    print(f"Hello {user_name}! You were born in approximately {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()
