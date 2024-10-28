def keys_with_values_greater_than(dictionary, n):
    result = []
    for key, value in dictionary.items():
        if value > n:
            result.append(key)
    return result

# Example usage
example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
result = keys_with_values_greater_than(example_dict, n)
print("Keys with values greater than", n, ":", result)
