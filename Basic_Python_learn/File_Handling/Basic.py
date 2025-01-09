# Q1. how to open file ?

# FIle Handling 
# Basic Operation That-Write,Read,Open,Change Data
# file=open("file_name",mode='')

# file=open("C:\Users\sande\Python\Day-5\demo.txt",'')
# for i in file:
#     print(i)


# file = open("demo.txt", mode="r")
# for i in file: 
#     print(i, end="")

# HOw open No exit File
# file=open("JD.py",mode='w')


# Method -01
# defulat Mode(Read mode)
file=open("demo.txt")
for i in file:
    print(i)

file.close()
# Method -02
# file=open("JD.py")
# print(file.read())



# Method 03
# Using with keyword 
# When we open file then we must to close file 
# We use method one and second that not close file we use keyword "close" then file will close
# so we are use "with" keyword that close autometically
# with open("demo.txt") as file:
#     print(file.read())