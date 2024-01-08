import sys
from ft_filter import ft_filter


def filter_words_by_length(words, length_threshold):
    """
    Filter words based on length.

    Args:
    - words (list): List of words.
    - length_threshold (int): Minimum length to include a word.

    Returns:
    - list: Filtered list of words.
    """
    return list(ft_filter(lambda word: len(word) > length_threshold, words))


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer

    Returns a list of words that are longer than the integer.
    """
    try:
        # Check the number of command-line arguments
        if len(sys.argv) != 3:
            raise AssertionError("Exactly two arguments (string and integer) are required.")

        text = sys.argv[1]
        length_threshold = int(sys.argv[2])

        # Validate argument types
        if not (isinstance(text, str) and isinstance(length_threshold, int)):
            raise AssertionError("Invalid argument types.")

        # Split the input string into words and filter based on length
        words = text.split()
        filtered_words = filter_words_by_length(words, length_threshold)

        print(filtered_words)

    except ValueError as error:
        print("ValueError:", error)
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
