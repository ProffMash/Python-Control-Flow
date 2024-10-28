def tuples_to_dict(tuples_list):
    return {key: value for key, value in tuples_list}

# Example usage:
input_tuples = [("apple", 5), ("banana", 3), ("orange", 7)]
result = tuples_to_dict(input_tuples)
print(result)  
