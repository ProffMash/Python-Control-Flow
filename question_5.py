def print_even_keys(data):
    for key, value in data.items():
        if value % 2 == 0:
            print(key)

# Example usage
example_dict = {'a': 2, 'b': 3, 'c': 4}
print("Keys with even values:")
print_even_keys(example_dict)
