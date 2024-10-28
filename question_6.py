def find_largest_number(numbers):
    largest = numbers[0] 
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers_tuple = (10, 20, 30, 40, 50)
result = find_largest_number(numbers_tuple)
print("The largest number is:", result)
