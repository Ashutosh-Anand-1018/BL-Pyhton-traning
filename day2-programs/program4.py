# Program to get friend's name and place of stay, print using f-string
input_data = input("Enter name and place: ")

name, place = input_data.split(", ")

print(f"Name of my friend is {name} and his/her place of stay is {place}.")