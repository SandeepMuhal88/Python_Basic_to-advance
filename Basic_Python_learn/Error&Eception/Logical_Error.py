def calculate_average(numbers):
    total=0
    for i in numbers:
        total+=numbers   #Forget the divide by len(numbers)
    return total

print(calculate_average([1,2,3,4,5,6]))

#  Example: Calculating average
# def calculate_average(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total  # Forgot to divide by len(numbers)

# print(calculate_average([1, 2, 3]))  # Returns sum instead of average