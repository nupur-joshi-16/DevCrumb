# operations on Tuples

fruits = ("Ram", "Shyam", 100, True, 100.50)
print(fruits)
temp_fruits = list(fruits)
print(temp_fruits)
temp_fruits.append(999) #add item
print(fruits)
print(temp_fruits)
temp_fruits.pop(2) #remove item
print(temp_fruits)
temp_fruits[3] = False #Change item
print(temp_fruits) 

fruits = tuple(temp_fruits) #just like this we can change tuple indirectly

print(fruits)

fruits_count = fruits.count(999)
print(fruits_count)

fruits_index = fruits.index(True)
print(fruits_index)

fruits_len = len(fruits)
print(fruits_len)