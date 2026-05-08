def calculate_sqrt(x:int):
    """
    This function takes a integer number and then returns the square root of that number.
    """
    if x < 0:
        return "Cannot calculate square root of a negative number."
    elif x == 0:
        return 0
    else:
        sqrt = x ** 0.5
        return sqrt
number = int(input("Enter a number: "))
result = calculate_sqrt(number)
print(f"The square root of {number:.2f} is: {result:.2f}")