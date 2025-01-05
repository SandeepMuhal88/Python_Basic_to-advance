# Number Classification
# Write a program that takes a number as input and classifies it:
# Positive and even
# Positive and odd
# Negative
# Zero

# num=int(input("Enter a number to check:-"))
# Method frist:
# if num>0 and num%2==0:
#     print("Number is Positive and Even")
# elif num>0 and num%2!=0:
#     print("Number is positive and Odd number>>>")
# elif num<0:
#     print("Number is Negative!!")
# else:
#     print("Number is Zero>>")

# Method -02
num=int(input("Enter a number to check:-"))
if num>0:
    if num%2==0:
        print("Number is positive ansd Even Number👌👍😁")
    else:
        print("Number is Positive and Odd number>>")
elif num<0:
    if num%2==0:
        print("Number is Negative ansd Even Number👌👍😁")
    else:
        print("Number is Negative and Odd number>>")
else:
    print("Number is zero!!")