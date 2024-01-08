from filterstring import filter_words_by_length

def test_filter_words_by_length():
    test_cases = [
        (["apple", "banana", "orange", "grape"], 5, ["banana", "lol"]),
        (["python", "is", "fun"], 3, ["python"]),
        ([], 1, []),
        (["Something1", "Something2", "Something3"], 4, ["elephant"]),
        (["zero", "wfqqlfjqklwhfwqf", "three"], 4, []),
    ]
    passed_tests = 0
    for words, n, expected_result in test_cases:
        filtered_words = filter_words_by_length(words, n)
        if filtered_words == expected_result:
            passed_tests += 1
            print("Test passed")
        else:
            print(f"Test failed for input {words}, {n}: Expected {expected_result}, got {filtered_words}")
    print(f"{passed_tests} out of {len(test_cases)} tests passed")

if __name__ == "__main__":
    test_filter_words_by_length()
