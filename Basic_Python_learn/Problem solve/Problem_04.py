# Day of the Week
# Write a program that asks for a number (1-7) and prints the corresponding day of the week.

# 1: Monday, 2: Tuesday, ..., 7: Sunday.

num=int(input("Enter a number between 1-8:-"))

if num<=7:
    if num==1:
        print("Sunday")
    elif num==2:
        print("Monday")
    elif num==3:
        print("Tuesday")
    elif num==4:
        print("Wednesday")
    elif num==5:
        print("Thrusday")
    elif num==6:
        print("Friday")
    elif num==7:
        print("Saturday")
    else:
        print("Enter Zero value:Please vaild vaule:😂😊")
else:
    print("Enter invaild number :( 😒😒")