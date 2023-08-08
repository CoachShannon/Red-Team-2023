city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
capitals = (('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9))

for capital in capitals:
    print('Name:', capital [0], ', Country:', capital[1], ' Population:',  capital[2])
    
user_data = ('John', 'American', 1995, [138, 141, 160])

#even if a list is in a tuple the data in the list is still mutuable
user_data[3].append(177)
print(user_data)