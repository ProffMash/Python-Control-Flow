def remove_duplicates():
    # Input
    user_input = input("Enter a list of numbers separated by spaces: ")
    lst = user_input.split()  # Split input by spaces

    # Convert each item to an integer (assuming the list contains numbers)
    lst = [int(item) for item in lst]

    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

result = remove_duplicates()
print("List without duplicates:", result)
