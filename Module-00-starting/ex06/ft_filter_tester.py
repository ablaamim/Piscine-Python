from ft_filter import custom_filter

# Test cases:

# Test 1: Filtering based on a function (even numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, None]
filtered_numbers_function = custom_filter(lambda x: x % 2 == 0, numbers)
print(list(filtered_numbers_function))  # Output: [2, 4, 6, 8]

# Test 2: Filtering based on a function (length of strings)
words = ["apple", "banana", "orange", "grape"]
filtered_words_function = custom_filter(lambda word: len(word) > 5, words)
print(list(filtered_words_function))  # Output: ['banana', 'orange']

# Test 3: Filtering based on None (truthy values)
values = [0, 1, "", "hello", None, [1, 2, 3]]
filtered_values_none = custom_filter(None, values)
print(list(filtered_values_none))  # Output: [1, 'hello', [1, 2, 3]]

# Test 4: Filtering based on a non-callable (truthy values)
names = ["Alice", "", "Bob", None, "Charlie"]
filtered_names_non_callable = custom_filter(42, names)
print(list(filtered_names_non_callable))  # Output: ['Alice', 'Bob', 'Charlie']
