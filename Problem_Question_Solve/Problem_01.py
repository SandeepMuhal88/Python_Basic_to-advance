# Q. Program to add to numbers

# a,b=map(int,input("Enter Two Numbers:-").split(','))
# sum=a+b
# print("Sum Of two numbers:-",sum)
# Q. write a program to print name
# Example
# 1. R a m
# name=input("Enter your name=")
# for i in name:
#     print(i,end=" ")

# Q. If input is "Rama krishna" then output is first and last character
# name=input("Enter a name:-")
# print(name[0]+name[-1])


# Q convert string to list
# Using Type casting
# str=input("Enter your name:-")
# l1=list(str)
# print(l1)

# Q convert list to string
l1=['S','O','N','I','Y','A',' ','Sandeep','Muhal']
# First method

# for i in l1:
#     print(i,end="")
l2="".join(l1)
print(l2)
print(type(l2))