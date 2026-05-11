def slice_string(input_string):
    if len(input_string) < 3:
        return "Input string must be at least 3 characters long."
    first = input_string[0]
    middle_idx = len(input_string) // 2
    middle = input_string[middle_idx]
    last = input_string[-1]
    return first + middle + last
# Example usage
input_str = input("Enter a string: ")
result = slice_string(input_str)
print("String after combining first middle and last is: ", result)