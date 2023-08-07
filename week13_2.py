# module 5: Data collections - Tuples, Dictionaries, and Tables

first = input('Enter first number:')
second = input('Enter second number:')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)



first = input('Enter first number:')
second = input('Enter second number:')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)



top_cities = ["New York City", "Los Angeles", "Boston", "Nashville", "Charlotte"]
top_cities[0], top_cities[3] = top_cities[3], top_cities[0]
print(top_cities)



top_cities = ["New York City", "Los Angeles", "Boston", "Nashville", "Charlotte"]
top_cities.sort()
print(top_cities)


#sort is a method that permenatly changes the order of the list, "sorting inplace"
random_numbers = [-2, -5, 0, 6, 12, -11]
random_numbers.sort
print(random_numbers)


#sorted is a general purpose function. It takes the list as an arguement and 
#returns a new list without affecting the original list
random_numbers = [-2, -5, 0, 6, 12, -11]
random_numbers.sort(reverse=True)
print(random_numbers)


# 
top_cities = ["New York City", "Los Angeles", "Boston", "Nashville", "Charlotte"]
print(sorted(top_cities))
print(top_cities)