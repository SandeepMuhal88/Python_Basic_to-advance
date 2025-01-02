# Identity Operators 


"""Identity Operators in Python
Identity operators are used to compare the memory locations of two objects. 
They determine whether two objects are the same object (i.e., they share the same memory address).
Python provides two identity operators:"""
x=[0,2,3]
y=x
z=[0,2,3]
print(y is x) #return true
print(y is z) #return false
# Use is not
print(y is not z)