# Add items in tuple using list

thistuple = ("apple", "banana", "cherry")
y = list(thistuple) 
y.append("orange") 
thistuple = tuple(y)
print(thistuple)