numbers = []
for i in range(1, 100):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(1, 101)]
print(numbers)

numbers = [i for i in range(1, 101) if i %3 != 0]
print(numbers)
