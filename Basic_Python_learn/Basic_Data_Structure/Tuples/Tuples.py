t1=(1,2,3,45)
print(t1)
print(type(t1))
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(len(t1))

t2=("Sandeep","Muhal",45,65,78,98,100)
print(t2)
print(type(t2))
print(t2[0])
print(t2[1])
print(t2[2])
print(t2[3])
print(t2[4])
print(t2[5])
print(t2[6])
print(len(t2))
# Defining tuples
t1 = (1, 2, 3)              # Tuple with integers
t2 = ("a", "b", "c")        # Tuple with strings
t3 = (1, "a", 3.14)         # Tuple with mixed types
t4 = (5,)                   # Single-element tuple (note the trailing comma)

# Accessing elements
print(t1[0])                # Output: 1
print(t2[1])                # Output: "b"
print(t3[2])                # Output: 3.14
print(t4[0])                # Output: 5

# Modifying elements using Typecastion
t1 = (1, 2, 3)
t2 = list(t1)               # Convert tuple to list
t2[1] = 4                   # Modify the list
t1 = tuple(t2)             # Convert list back to tuple

# Adding elements
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2                # Concatenate tuples
print(t3)                   # Output: (1, 2, 3, 4, 5)

# Common Use Cases
# Grouping related data (e.g., coordinates (x, y) or RGB colors (r, g, b)).
# Returning multiple values from a function.
# Ensuring data integrity (since tuples are immutable).