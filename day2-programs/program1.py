"""Program to get names of 3 people and print them a greeting message by 
reversing the order in which their name appear using f-string"""
names = input("Enter name of 3 people:" )
name1, name2, name3 = names.split(", ")
print(f"Hello {name3}, {name2} and {name1}.")