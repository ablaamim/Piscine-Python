def ft_filter(criteria, data):
    """Custom filter implementation\n
    Returns a generator yielding items from data based on\n
    the given criteria."""
    if callable(criteria):
        return (item for item in data if criteria(item))
    return (item for item in data if item)
