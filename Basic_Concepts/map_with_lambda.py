# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


#add two lists using map and lamda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# map fun to which mpa object (iterator) of the results after applying the given functtion to each item of a given iterable(list,tuple)
# map (func,iter)


