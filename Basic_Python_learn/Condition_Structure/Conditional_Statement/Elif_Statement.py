print("perform elif statement condition:)")

# a=int(input("Enter first value:-"))
# b=int(input("Enter second value:-"))
# c=int(input("Enter third value:-"))
# if a>b:
#     print("a is gretest..")
# elif b>c:
#     print("b is gretest..")
# else:
#     print("c is gretest..")

# Marks >= 90: Grade A
# Marks >= 75 and < 90: Grade B
# Marks >= 50 and < 75: Grade C
# Marks < 50: Grade F
marks=int(input("Enter your masks:"))
if marks>=90:
    print("Greet You earn 'A Gread'")
elif marks>=75 and marks<90:
    print("You earn:'B Grade'")
elif marks>=50 and marks<75:
    print("You earn'C Grade'")
else:
    print("Try next time:)")

