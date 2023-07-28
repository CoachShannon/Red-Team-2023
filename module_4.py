user_age = int(input('How old are you? '))
if user_age > 35:
    print('Your getting up there huh.')
    print('But with age comes wisdom!')
elif user_age == 35:
    print('Wow. Your in the prime of your life, enjoy!')
else:
    print('Still got plenty of time!')
    print('Thats if you make it that long, ya big dummy.')
    
# available logical operators
#   < less than
#   > greater than
#  <= less than or equal 
#  >= greater than or equal
#  == equals
#  != not equals

password = input('Do you know the secret password?')
if password != '--secret':
    print('not correct')
else: 
    print('correct password')
    
#joining multiple conditions
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German exchange programme')
else: 
    print('Sorry, you must be a citizen to qualify for the exchange programme')
    
    
user_country = input('What is your country?')
if not user_country == 'Germany':
    print('your not from Germany?!')
else:
    print('your not from Germany!!')
    
    
    
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
    print('You qualify')
else:
    print('You dont\'t qualify!')