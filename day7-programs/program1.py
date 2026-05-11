input_list = []
for i in range(5):
    num = int(input("Enter a number: "))
    input_list.append(num)
print("Input list:", input_list,"\n")
double_elements = list(map(lambda x: x * 2, input_list))
print(double_elements)