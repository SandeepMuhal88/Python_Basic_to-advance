t1=(1,2,3,4,5,6,7,8,9,10,2,5,6,3,2,2,1,2,5,2,3,6,2)
t2=(1,5,6,3,2)
print("The Length of Tuple:-",len(t1))
print("Count of 2 in Tuple:-",t1.count(2))
print("Index of 2 in Tuple:-",t1.index(2))
print("Index of 2 in Tuple:-",t1.index(2,8))
print("Index of 2 in Tuple:-",t1.index(2,8,15))
t4=t1   # Shallow copy
print("Id of t1:-",id(t1))
print("Id of t4:-",id(t4))

# input From user as tuple
# t1=()
# num=int(input("Enter a number:-"))
# for i in range(num):
#     item=input("Enter Items in tuple:-")
#     t1=t1+(item,)
# print(t1)

# Method -02
l1=[]
num=int(input("Enter a number:-"))
for i in range(num):
    item=input("Enter Items in tuple:-")
    l1.append(item)
t1=tuple(l1)
print(t1)