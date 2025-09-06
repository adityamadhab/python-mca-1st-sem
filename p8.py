# Program to show use of identity and membership operators in Python

# Identity operators: is, is not
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)      # True, same object
print("x is z:", x is z)      # False, different objects with same content
print("x is not z:", x is not z)  # True

# Membership operators: in, not in
nums = [1, 2, 3, 4, 5]
print("2 in nums:", 2 in nums)
print("6 in nums:", 6 in nums)
print("4 not in nums:", 4 not in nums)

text = "hello world"
print("'world' in text:", 'world' in text)
print("'python' not in text:", 'python' not in text)
