user_data = ('John', 'American', 2014)
print(len(user_data))

user_data = ('John', 'American', 2014)
if 'American' in user_data:
    print('This person is from the US!')

user_data = ('John', 'American', 2014)
for element in user_data:
    print(element)
    
#using the plus sign, you create a new tuple and add to the same
#variable.
user_data = ('John', 'American', 2014) + ('teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

#when do you use lists vs tuples
#lists are used when you have multiple valuse of the same data type
Knoxville_temps(98, 86, 94, 72, 70, 101)
male_names('Adam', 'Jesse', 'Shannon')

#tuples are used when you have a bunch of values that are somehow
#related
user_data = ('John', 'American', 1995)

