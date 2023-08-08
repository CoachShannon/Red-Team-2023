#continuation of coursework

list_original = [1, 2, 3]
list_new = list_original
list_original [0] = -5
print('original:', list_original, '\nNew:',list_new)


list_original = [1, 2, 3]
list_new = list_original[:]
list_original [0] = -5
print('original:', list_original, '\nNew:',list_new)


list_original = [1, 2, 3]
list_new = list_original[:2]
list_original [0] = -5
print('original:', list_original, '\nNew:',list_new)
