# nested if
answer_a = input('Do you like travellin? y/n:')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
    if answer_b == 'y': 
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else: 
    print('Sorry to hear that!')
    
    
    

#nested if challenge
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')
  
  
  
#"while" and "for" loops

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')


for counter in range(1,11):
    print(counter)
print('Finished!')



#break and continue
while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
    
    
for i in range(1,21):
    if i % 5 == 0:
        continue
    print(i)