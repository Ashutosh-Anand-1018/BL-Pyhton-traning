def greet_user(name:str):
    """
    This function takes a string input for user's name and prints a greeting message.
    """
try:
    name = str(input("Enter your name: "))
    print(f"Hello, {name}!")
except ValueError as err:
    print("Try again. A {err} error occurred. Please enter a valid name.")