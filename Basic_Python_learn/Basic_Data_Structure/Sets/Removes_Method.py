s1={45,2,6,31,(12.,6,3,9,2,12,52,15),"Address",'Rajasthan'}
print(s1)
print(type(s1))
print(s1.pop())
# The output of s1.pop() being 2 in your code is due to the unordered nature of sets in Python.Python’s hashing mechanism determined 2 to be the first element based on the internal hash table used by the set. This behavior is implementation-dependent and can vary. For example:
# If you run the same code on a different Python interpreter or version,
# a different element might be popped.
# The behavior might even differ between different runs of the program.