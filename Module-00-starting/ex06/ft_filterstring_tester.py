from filterstring import filter_words_by_length


def simple_test():
    # Test Case 1
    words_1 = ["Hello", "The", "World"]
    n_1 = 4
    expected_result_1 = ["Hello", "World"]
    filtered_words_1 = filter_words_by_length(words_1, n_1)
    print(f"Test Case 1: {filtered_words_1 == expected_result_1}")

    # Test Case 2
    words_2 = ["Hello", "The", "World"]
    n_2 = 99
    expected_result_2 = []
    filtered_words_2 = filter_words_by_length(words_2, n_2)
    # print(filtered_words_2)
    print(f"Test Case 2: {filtered_words_2 == expected_result_2}")

    # Test Case 3
    words_3 = []
    n_3 = 1
    expected_result_3 = []
    filtered_words_3 = filter_words_by_length(words_3, n_3)
    print(f"Test Case 3: {filtered_words_3 == expected_result_3}")

    # Test Case 4
    words_4 = ["dog", "cat", "elephant"]
    n_4 = 4
    expected_result_4 = ["elephant"]
    filtered_words_4 = filter_words_by_length(words_4, n_4)
    print(f"Test Case 4: {filtered_words_4 == expected_result_4}")

    # Test Case 5
    words_5 = ["zero", "nani", "three", []]
    n_5 = 4
    expected_result_5 = ["three"]
    filtered_words_5 = filter_words_by_length(words_5, n_5)
    # print(filtered_words_5)
    print(f"Test Case 5: {filtered_words_5 == expected_result_5}")


if __name__ == "__main__":
    simple_test()
