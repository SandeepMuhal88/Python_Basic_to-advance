
# Membership Operators in Python
# Membership operators are used to test whether a value or variable exists
# in a sequence (e.g., strings, lists, tuples, sets, dictionaries).

# Python provides two membership operators:
# in
l1=[4,5,6,9,3,4,100]
print(100 in l1) #return true
print(10000 in l1) #return false

# x=45
# print(10 in x)
# Error :-rgument of type 'int' is not iterable

x="I accept 365 days challenge"
print('accept' in x) #return true
print('Dasy' in x)  #return False

# not in operator
print("Use not in operator")
x=[1,2,3,6,5]
print(50 not in x)
sentence = "Python is fun"
print('Python' in sentence)  # Output: True
print('java' not in sentence)  # Output: True
