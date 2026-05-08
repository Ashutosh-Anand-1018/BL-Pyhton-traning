def greet(name:str):
    if name.isalpha():
        print(f"Hello, {name}! How are you doing today?")
    else:
        print("Please enter a valid name consisting of only letters.")  
user_name = input("Please enter your name: ")
greet(user_name)