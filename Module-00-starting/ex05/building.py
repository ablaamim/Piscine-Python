import string
import sys


def calculate_sums(input_string):
    """Calculate and display the sums of various \
    character types in the input string."""
    char_counts = {
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'digits': 0,
        'spaces': 0
    }

    for char in input_string:
        if char.isupper():
            char_counts['upper'] += 1
        elif char.islower():
            char_counts['lower'] += 1
        elif char in string.punctuation:
            char_counts['punctuation'] += 1
        elif char.isspace():
            char_counts['spaces'] += 1
        elif char.isdigit():
            char_counts['digits'] += 1

    total_characters = sum(char_counts.values())

    print(f"The text contains {total_characters} characters:")
    print(f"{char_counts['upper']} upper letters")
    print(f"{char_counts['lower']} lower letters")
    print(f"{char_counts['punctuation']} punctuation marks")
    print(f"{char_counts['spaces']} spaces")
    print(f"{char_counts['digits']} digits")


def main():
    """Main function to handle command-line\
     arguments and execute the program."""
    try:
        # Check the number of command-line arguments
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        # Retrieve the input string from the command-line argument
        if len(sys.argv) == 2:
            input_string = sys.argv[1]
        else:
            try:
                input_string = input("What is the text to count?\n")
            except EOFError:
                print("\nError: End of input reached. Exiting.")
                sys.exit(1)
            except KeyboardInterrupt:
                print("\nError: Keyboard interrupt. Exiting.")
                sys.exit(1)

        # Check if the input is a valid string
        if not isinstance(input_string, str):
            raise ValueError("Provided input is not a valid string.")

        # Calculate and display character sums
        calculate_sums(input_string)

    except (AssertionError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
