def has_pair_with_sum():
    # Input
    user_input = input("Enter a list of integers separated by spaces: ")
    
    # Convert the input string to a list of integers
    nums = list(map(int, user_input.split()))

    # sum Input
    target_sum = int(input("Enter the target sum: "))

    seen = set() 
    for num in nums:
        complement = target_sum - num  # Calculate the required complement
        if complement in seen:
            return True  # Found a pair
        seen.add(num)  # Add the current number to the seen set
    return False  # No pairs found

# Example usage
result = has_pair_with_sum()
print("Pair exists:", result)
