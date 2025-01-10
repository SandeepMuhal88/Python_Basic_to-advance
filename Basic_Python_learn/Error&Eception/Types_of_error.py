# Mixing incompatible types
# text = "Hello"
# number = 5
# result = text + number  # Can't add string and integer

# def add(a,b):
#     return a+b

# x='Sandeep'
# y=90
# print(add(x,y))

# there is give a error
# Output
# Traceback (most recent call last):
#   File "c:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\Error&Eception\Types_of_error.py", line 11, in <module>
#     print(add(x,y))
#           ^^^^^^^^
#   File "c:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\Error&Eception\Types_of_error.py", line 7, in add
#     return a+b
#            ~^~
# TypeError: can only concatenate str (not "int") to str
# PS C:\Users\sande\Desktop\Python_Basic_to_Advance> 

# ) ValueError
# Invalid value for conversion
# number = int("abc")  # Can't convert "abc" to integer
# a=int(input("Enter your name:-"))
# print(a)

# Enter your name:-Sandeep MUhal
# Traceback (most recent call last):
#   File "c:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\Error&Eception\Types_of_error.py", line 28, in <module>
#     a=int(input("Enter your name:-"))
#       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'Sandeep MUhal