# file=open("File_name",mode='+a')

# file=open(r'C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basicinfo.txt',mode='r')
# for i in file:
#     print(i)
# file.close()

# File=open(r"C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basicinfo.txt",'r')
# content=File.read()
# print(content)
# file.close()
# We don't use close so we defin with function

# with open(r'C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basicinfo.txt','r') as file:
#     content=file.read()
# print(content)


# Read mrhtod 
# Readline
# with open(r'C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basicinfo.txt','r') as file:
#     content=file.readline()
#     print(content)

# Readlines()
# That print in the list form

with open(r'C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basicinfo.txt','r') as files:
    content=files.readlines()
    print(content)

