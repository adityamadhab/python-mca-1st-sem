
# Program to show implicit and explicit type casting in Python

# Implicit type casting
num_int = 5
num_float = 2.5
result = num_int + num_float  # int is implicitly cast to float
print("Implicit Type Casting:")
print(str(num_int) + " (int) + " + str(num_float) + " (float) = " + str(result) + " (" + str(type(result)) + ")")

# Explicit type casting
num_str = "100"
num_int2 = int(num_str)  # string explicitly cast to int
num_float2 = float(num_int2)  # int explicitly cast to float
print("\nExplicit Type Casting:")
print('"' + num_str + '" (str) -> ' + str(num_int2) + ' (int) -> ' + str(num_float2) + ' (float)')
print("Types: " + str(type(num_str)) + ", " + str(type(num_int2)) + ", " + str(type(num_float2)))
