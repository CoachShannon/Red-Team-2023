#list checking presence
for char in 'happy message':
    print(char)
    
    
    
invited_guests = ['Kate', 'Joe', 'Quan', 'Bre', 'Bron', 'Nacyn']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome! ')
else:
    print('Sorry your not invited. ')
    
    
    
#Reversal of the code above
#Check linse (9,20) for refrence
invited_guests = ['Kate', 'Joe', 'Quan', 'Bre', 'Bron', 'Nacyn']
name = input('What is your name? ')
if name not in invited_guests:
    print('Sorry your not invited. ')
else:
    print('Welcome! ')
    


name_original = 'Jon Snow'
name_new = name_original
name_original ='Daenerys Targaryen'
print(name_original, name_new)


list_original = [1, 2, 3]
list_new = list_original
list_original[0] =  -5
print('Original:', list_original, '\nNew:', list_new)