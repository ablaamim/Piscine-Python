from sos import encode_to_morse


def run_simple_tests():
    # Test Case 1
    input_text_1 = "Hello World"
    expected_result_1 = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    result_1 = encode_to_morse(input_text_1)
    print(f"Test Case 1: {result_1 == expected_result_1}")

    # Test Case 2
    input_text_2 = "Python is fun"
    expected_result_2 = ".--. -.-- - .... --- -. / .. ... / ..-. ..- -."
    result_2 = encode_to_morse(input_text_2)
    print(f"Test Case 2: {result_2 == expected_result_2}")

    # Test Case 3
    input_text_3 = ""
    expected_result_3 = ""
    result_3 = encode_to_morse(input_text_3)
    print(f"Test Case 3: {result_3 == expected_result_3}")

    # Test Case 4
    input_text_4 = "abc def ghi"
    expected_result_4 = ".- -... -.-. / -.. . ..-. / --. .... .."
    result_4 = encode_to_morse(input_text_4)
    print(f"Test Case 4: {result_4 == expected_result_4}")

    # Test Case 5
    input_text_5 = "One Two Three"
    expected_result_5 = "--- -. . / - .-- --- / - .... .-. . ."
    result_5 = encode_to_morse(input_text_5)

    # print(result_5)
    print(f"Test Case 5: {result_5 == expected_result_5}")

    # Test Case 6
    input_text_6 = "Zero Nani Three"
    expected_result_6 = "--.. . .-. --- / -. .- -. .. / - .... .-. . ."
    result_6 = encode_to_morse(input_text_6)
    # print(result_6)
    print(f"Test Case 6: {result_6 == expected_result_6}")


if __name__ == "__main__":
    run_simple_tests()
