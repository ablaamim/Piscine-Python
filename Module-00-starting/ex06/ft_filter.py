def custom_filter(criteria, data):
    """Custom filter implementation\n
    Returns a generator yielding items from data based on the given criteria."""
    if callable(criteria):
        return (item for item in data if criteria(item))
    return (item for item in data if item)

# Example usage:
elements = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Using a function to filter elements divisible by 10
filtered_elements_function = custom_filter(lambda x: x % 10 == 0, elements)
print(list(filtered_elements_function))

# Using None to filter truthy values
filtered_elements_none = custom_filter(None, elements)
print(list(filtered_elements_none))
