# # Memory Error example
# list = [1] * (10**8) * (10**8)  # Tries to create huge list

# # Overflow Error example
# import sys
# number = sys.maxsize ** sys.maxsize

l1=[2]*(10**9)*(10**4)



#   File "c:\Users\sande\Desktop\Python_Basic_to_Advance\Basic_Python_learn\Error&Eception\System_error.py", line 8, in <module>
#     l1=[2]*(10**9)*(10**4)
#        ~~~~~~~~~~~^^~~~~~~
# MemoryError
# PS C:\Users\sande\Desktop\Python_Basic_to_Advance> & C:/Users/sande/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/sande/Desktop/Python_Basic_to_Advance/Basic_Python_learn/Error&Eception/System_error.py"
# Traceback (most recent call last):
#     l1=[2]*(10**9)*(10**4)
#        ~~~~~~~~~~~^^~~~~~~
# MemoryError
# PS C:\Users\sande\Desktop\Python_Basic_to_Advance> & C:/Users/sande/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/sande/Desktop/Python_Basic_to_Advance/Basic_Python_learn/Error&Eception/System_error.py"
# object address  : 00000246FF4ED060
# object refcount : 3
# object type     : 00007FF83CA4AE30
# object type name: MemoryError
# object repr     : MemoryError()