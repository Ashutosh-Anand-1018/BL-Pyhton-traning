places = []
for i in range(5):
    place = input(f"Enter name of place {i+1}: ")
    places.append(place)
print("Places stored in the list: ", places)
for i in places:
    print(i.upper(),end = ", ")
