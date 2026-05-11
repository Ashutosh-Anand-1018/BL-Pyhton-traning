colors = ["Red", "Green", "Pink", "Blue", "Black", "Purple", "Yellow", "Magenta", "Brown"]

print("Colors List :", colors)

indices_to_remove = [0, 2, 5]
indices_to_remove.sort(reverse=True)

for index in indices_to_remove:
    colors.pop(index)

print("Revised color list :", colors)
