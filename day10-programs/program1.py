import sys
import timeit
tuple1 = (1, 2, 3, 4, 5)
list1 = [1, 2, 3, 4, 5]
print("Size of tuple: ", sys.getsizeof(tuple1), "bytes")
print("Size of list: ", sys.getsizeof(list1), "bytes")
print("Time taken for tuple (in seconds): ", timeit.timeit(stmt="tuple1 = (1, 2, 3, 4, 5)", number=1000000))
print("Time taken for list (in seconds): ", timeit.timeit(stmt="list1 = [1, 2, 3, 4, 5]", number=1000000))