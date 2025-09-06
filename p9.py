# Program to show different uses of built-in string functions in Python

s = "  Hello World! 123  "

print("Original string:", repr(s))
print("Length:", len(s))
print("Lowercase:", s.lower())
print("Uppercase:", s.upper())
print("Count of 'l':", s.count('l'))
print("Find 'World':", s.find('World'))
print("Index of 'o':", s.index('o'))
print("Endswith '123':", s.endswith('123'))
print("Startswith '  He':", s.startswith('  He'))
print("Is Alphanumeric:", s.isalnum())
print("Is Space:", s.isspace())
print("Is Lower:", s.islower())
print("Is Upper:", s.isupper())
print("Left strip:", repr(s.lstrip()))
print("Right strip:", repr(s.rstrip()))
print("Strip:", repr(s.strip()))
print("Replace 'World' with 'Python':", s.replace('World', 'Python'))
print("Join with '-':", '-'.join(['Hello', 'World']))

# f-string example
name = "Alice"
age = 30
print(f"f-string: Name is {name}, Age is {age}")

# format method
print("Format: Name is {}, Age is {}".format(name, age))

# Partition
print("Partition on 'World':", s.partition('World'))

# Split
print("Split on space:", s.split())
