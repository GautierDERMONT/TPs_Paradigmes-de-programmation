#====Question 1.1====:
square = lambda x: x ** 2

#====Question 1.2====:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print("Carrés des nombres :", squared_numbers)

#====Question 1.3====:
add = lambda a, b: a + b

#====Question 1.4====:
from functools import reduce
total_sum = reduce(add, numbers)
print("Somme totale :", total_sum)