# Created by: Vova
# Created on: 3 November 2026
# This program determines if a year entered by the user is a leap year.


def main():
    # Get the year as input string
    year_string = input("Enter a year: ")

    # Try to convert input to integer to handle invalid input
    try:
        year_integer = int(year_string)

        # Check if the year is positive
        if year_integer > 0:
            # Check leap year conditions using nested if statements
            if year_integer % 4 == 0:
                if year_integer % 100 == 0:
                    if year_integer % 400 == 0:
                        print(f"{year_integer} is a leap year.")
                    else:
                        print(f"{year_integer} is NOT a leap year.")
                else:
                    print(f"{year_integer} is a leap year.")
            else:
                print(f"{year_integer} is NOT a leap year.")
        else:
            print("Please enter a valid positive year.")

    except ValueError:
        print("Invalid input! Please enter a valid integer year.")


if __name__ == "__main__":
    main()
