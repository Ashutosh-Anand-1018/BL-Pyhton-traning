import regex as re

def check_digits(string):
    digits = re.findall(r'\d', string)
    return digits

input_str = input("Enter a string: ")
digits_found = check_digits(input_str)
if digits_found:
    print("Digits found in the string: ", digits_found)
else:    
    print("No digits found in the string.")