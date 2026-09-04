@@ -1,21 +1,21 @@
"""TODO: Replace with a one-line summary of the program's purpose (<73 chars).
"""Calculates a user's approximate birth year based on their age.
Input:
    TODO: Replace with a major input, including its type and source.
    TODO: Replace with another major input, or delete this TODO line.
    TODO: Replace with another major input, or delete this TODO line.
    user_name: The user's name as a string from keyboard input.
    user_age: The user's age as an integer from keyboard input.
Process:
    TODO: Replace with a major processing step.
    Subtract the user's age from the current year to find their birth year.
Output:
    TODO: Replace with a major output, including its type and destination.
    A personalized greeting with the calculated birth year to the console.
Typical usage example:
    TODO: Replace with the input prompt and original name-input example.
    TODO: Replace with the input prompt and original age-input example.
    TODO: Replace with the resulting output from those inputs.
    Enter your name: Darrius Brooks
    Enter your age: 26
    Hello Darrius Brooks! You were born in or around 2000.
"""

# === Imports ===
from datetime import date

@@ -29,21 +29,16 @@ def main() -> None:
    """Run the name-age program."""

    # Get user input.
    # TODO: Replace with code to get user's name as a string. See zyBooks 1.3.
    # TODO: Replace with code to get user's age as an integer. See zyBooks 2.6.
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
    # TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.
    print(f"Hello {user_name}! You were born in or around {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
Footer
