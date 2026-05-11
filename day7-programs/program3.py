def transpose_matrix(list1,list2,list3):
    transposed_matrix = []
    for i in range(len(list1)):
        transposed_matrix.append([list1[i], list2[i], list3[i]])
    return transposed_matrix
list1 = [1, 2, 3]
list2 = [4, 5, 6]  
list3 = [7, 8, 9]
result = transpose_matrix(list1, list2, list3)
print("Transposed Matrix:")
for row in result:
    print(row)
