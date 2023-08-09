def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)

#the numbers in the average are considered arguments
get_average([5.0, 2.2, 3.6, 0.7, 9.4])


def print_letter_count(text, letter):
    counter = 0
    for chicken in text:
        if chicken == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
print_letter_count('Welcome', 'e')
print_letter_count('People say nothing is impossible, but I do nothing every day.', 'a')

#positional arguments, provide search field then what you want to find.