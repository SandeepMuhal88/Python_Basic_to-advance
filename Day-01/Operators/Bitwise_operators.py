# Bitwise Operators in Python
# Bitwise operators are used to perform operations on binary representations of integers at the bit level.
# These operators directly manipulate the bits of numbers
# Operation has own properties
# AND(&), OR(|), XOR(^),NOT(~),Lift shift(>>>),right shift(<<<)
# AND(&)
x=10 #binary = 1010
y=11 #binary= 1011
z=6  #binary= 0001
print(x&y) #binary =1010
# OR(|)
print("OR operation:-",x|y) # 1011 (Desimal=11)
print("XOR operation:-",x^y)  # 0001
print("NOT operation:-",~z) #
a=5
print(a>>1)