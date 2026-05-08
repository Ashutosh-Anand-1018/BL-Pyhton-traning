"""
This program takes names of 5 places as input from the user, then prints the names of those places in 2 format
1. print in a single line.
2. print in multi line format with a gap of 2 lines
"""
places = input("Enter names of the places: ").split(", ")
places_list = list(places)

#Method-1 print the names of places in a single line
print("My favorite places are", end=" ")
for i in range(len(places_list)):
    if i != len(places_list)-1:
        print(places_list[i],end=", ")
    else:
        print(places_list[i])

#Method-2 print the names of places with a gap of 2 lines
print("My favorite places are", end="\n")
for i in range(len(places_list)):
    if i != len(places_list)-1:
        print(places_list[i],end="\n\n")
    else:
        print(places_list[i])