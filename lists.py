var = []

print(type(var))

print(type("Hello"))

var2 = [151, 152, 153, 154, "007"]

print(var2)

var2 = var2 + [721] # not inplace

print(var2)

var2.append(445) # inplace function

print(var2)

print(dir(var2))

var2.reverse()
print(var2)
