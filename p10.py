# Program to show string concatenation in Python

str1 = "Hello"
str2 = "World"

# Using + operator
result1 = str1 + " " + str2
print("Using + operator:", result1)

# Using join()
result2 = " ".join([str1, str2])
print("Using join():", result2)

# Using % formatting
result3 = "%s %s" % (str1, str2)
print("Using %% formatting:", result3)

# Using format()
result4 = "{} {}".format(str1, str2)
print("Using format():", result4)

# Using f-string
result5 = f"{str1} {str2}"
print("Using f-string:", result5)
