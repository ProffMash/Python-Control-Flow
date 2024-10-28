def reverse_strings(strings):
    reversed_list = []
    for s in strings:
        reversed_list.append(s[::-1])
    return reversed_list

# Example usage
words = ["apple", "banana", "cherry"]
result = reverse_strings(words)
print("Reversed strings:", result)
