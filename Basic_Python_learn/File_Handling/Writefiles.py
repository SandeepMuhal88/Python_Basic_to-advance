# # Write method
# with open(r'C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basic.txt','w') as files:
#     content=files.write("Hellwow guyes!!")
#     print(content)


with open(r'C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basic.txt','w') as files:
   files.write("Namsate dosto swagat hai aapka mere naya video mai")
 
with open(r'C:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\File_Handling\Basic.txt','r') as rea:
    content=rea.readlines()
    print(content)