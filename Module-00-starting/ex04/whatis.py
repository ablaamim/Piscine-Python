import sys


def check_odd_even(number):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 whatis.py <integer>")
        sys.exit(1)
    # Try to convert the argument to an integer
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)
    # Check if the number is odd or even
    check_odd_even(number)
