#1st ex. is using 'Shadowing'
def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)


#2nd is using 'global' to assign a new value to the function
#try to avoid using the global variable
def show_truth():
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
    
mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)


#be careful when using append, del, sort on functions. You could accidently
#change a global function.
def show_truth():
    mysterious_var.append('New Surprise!')
    print(mysterious_var)

mysterious_var = ('Surprise!')
print(mysterious_var)
show_truth()
print(mysterious_var)
