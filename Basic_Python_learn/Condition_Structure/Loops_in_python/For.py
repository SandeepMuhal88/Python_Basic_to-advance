# Use For loops

# Loops in Python are fundamental programming concepts that allow you to execute a block of code multiple times
# . Python provides two main types of loops:

# 1. for Loop
# Used when you know the number of iterations or when you want to iterate over a sequence (like a list, string, or range)
# for item in sequence:
    # Code block
# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):  # i will take values 0, 1, 2, 3, 4
    print(i)


# Write a for loop to print numbers from 1 to 10.

num =int(input("Enter a number:-"))
for i in range(num+1):
    print(i)